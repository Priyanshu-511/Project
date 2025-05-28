import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize lists to store data
anime_name = []
year = []
score = []
votes = []
summary = []
episodes = []
stars = []
genere = []
image_url = []

# Set up Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Base URL for the IMDb list
base_url = "https://www.imdb.com/list/ls026392856/?page="

# Part 1: Extract data from list pages 1 to 3
for page in range(1, 4):  # Loop through pages 1, 2, 3
    url = f"{base_url}{page}"
    print(f"Processing page {page}/3: {url}")
    
    # Load the page
    driver.get(url)
    time.sleep(2)  # Wait for content to load

    # Get the page source
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Extract anime data from the list page
    anime_data = soup.find_all('div', class_='ipc-metadata-list-summary-item__c')
    print(f"Found {len(anime_data)} anime entries on page {page}")

    for i, anime in enumerate(anime_data):
        print(f"Processing anime {i+1}/{len(anime_data)} on page {page}")
        
        # Anime name
        name_elem = anime.find('h3', class_='ipc-title__text')
        name = name_elem.text.split(" ", 1)[1] if name_elem and len(name_elem.text.split(" ", 1)) > 1 else ""
        anime_name.append(name.strip())

        # Year
        year_elem = anime.find('span', class_='sc-4b408797-8 iurwGb dli-title-metadata-item')
        year.append(year_elem.text if year_elem else "")

        # Score
        score_elem = anime.find('span', class_='ipc-rating-star--rating')
        score.append(score_elem.text if score_elem else "")

        # Votes
        vote_elem = anime.find('span', class_='ipc-rating-star--voteCount')
        vote_count = re.search(r'\((.*?)\)', vote_elem.text).group(1) if vote_elem and re.search(r'\((.*?)\)', vote_elem.text) else ""
        votes.append(vote_count)

        # Summary
        summary_elem = anime.find('div', class_='ipc-html-content-inner-div')
        summary.append(summary_elem.text.strip() if summary_elem else "")

print("Part 1 completed. Moving to Part 2...")

# Part 2: Extract additional data from individual anime pages
links = []
for page in range(1, 4):  # Collect links from pages 1 to 3
    url = f"{base_url}{page}"
    driver.get(url)
    time.sleep(2)  # Wait for content to load
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    page_links = soup.find_all('a', class_='ipc-lockup-overlay ipc-focusable')
    page_links = [link for link in page_links if link.get('href') and link.get('href').startswith('/title/')]
    links.extend(page_links)
    print(f"Collected {len(page_links)} links from page {page}")

print(f"Total valid links found: {len(links)}")

# Set up requests session
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.imdb.com/",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}
session = requests.Session()
session.headers.update(headers)

for i, link in enumerate(links):
    href = link.get('href')
    url2 = f"https://www.imdb.com{href}"
    print(f"Processing link {i+1}/{len(links)}: {url2}")

    try:
        new_res = session.get(url2)
        new_res.raise_for_status()
        soup2 = BeautifulSoup(new_res.content, 'html.parser')

        # Episodes
        epi_elem = soup2.find('span', class_='ipc-title__subtext')
        episodes.append(epi_elem.text if epi_elem else "")

        # Stars
        star_elem = soup2.find('div', class_='ipc-metadata-list-item__content-container')
        stars.append(star_elem.text.strip() if star_elem else "")

        # Genre
        genre_div = soup2.find('div', class_='ipc-chip-list__scroller')
        genres = [tag.text.strip() for tag in genre_div.find_all('a')] if genre_div else []
        genere.append(" ".join(genres))

        # Image URL
        img_elem = soup2.find('img', class_='ipc-image')
        image_url.append(img_elem['src'] if img_elem and img_elem.get('src') else "")

    except requests.RequestException as e:
        print(f"Error fetching {url2}: {e}")
        episodes.append("")
        stars.append("")
        genere.append("")
        image_url.append("")
    
    # Add delay to avoid rate limiting
    time.sleep(0.5)

print("Part 2 completed. Creating DataFrame...")

# Ensure all lists are of equal length
max_len = max(len(anime_name), len(year), len(score), len(votes), len(summary), len(episodes), len(stars), len(genere), len(image_url))
lists = [anime_name, year, score, votes, summary, episodes, stars, genere, image_url]
for lst in lists:
    lst.extend([''] * (max_len - len(lst)))

# Create DataFrame
df = pd.DataFrame({
    "Anime name": anime_name,
    "Year": year,
    "Score": score,
    "Voting": votes,
    "Summary": summary,
    "Number of episode": episodes,
    "Stars": stars,
    "Genre": genere,
    "Image": image_url
})

# Ensure UTF-8 encoding for columns up to Genre
utf8_columns = ["Anime name", "Year", "Score", "Voting", "Summary", "Number of episode", "Stars", "Genre"]
for col in utf8_columns:
    df[col] = df[col].apply(lambda x: x.encode('utf-8').decode('utf-8') if isinstance(x, str) else str(x).encode('utf-8').decode('utf-8'))

# Save to JSON
df.to_json("movies.json", orient="records", indent=4, force_ascii=False)

# Verify JSON content
with open("movies.json", "w", encoding="utf-8") as f:
    json.dump(json.loads(df.to_json(orient="records", force_ascii=False)), f, indent=4, ensure_ascii=False)

print(f"Data successfully saved to movies.json with {len(anime_name)} entries")
driver.quit()