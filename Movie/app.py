import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
import json
import re

headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36"
    }

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
response = requests.get(url,headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

movie_name = []
year = []
runtime = []
score = []
votes = []
summary = []
director = []
crew = []
genere = []
image_url = []

movie_data = soup.findAll('div', attrs= {'class': 'ipc-metadata-list-summary-item__c'})

for store in movie_data:
    RElease = store.find('span', class_="sc-b189961a-8 kLaxqf cli-title-metadata-item").text
    year.append(RElease)
    print(year)
    
    time = store.find('div', class_="sc-b189961a-7 feoqjK cli-title-metadata").text
    runtime.append(time[4:].replace('m', 'm '))
    print(runtime)

    rating_span  = store.find('span', class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating").text
    imdb_rating = rating_span.split('\xa0')[0]
    score.append(imdb_rating)
    print(score)
    
    vote_span  = store.find('span', class_="ipc-rating-star--voteCount").text
    vote_count = re.search(r'\((.*?)\)', vote_span).group(1)
    votes.append(vote_count)
    print(votes)

    
print("part 1 is done. Now it is time to part 2")

links = soup.findAll('a', class_="ipc-title-link-wrapper")
del links[-7:]

for link in links:
    title_text = str(link)
    neww=(title_text.split())
    mews=neww[2].split('"')
    #print(mews[1])
    
    newURl = "https://www.imdb.com/"+mews[1]
    newRESponse = requests.get(newURl, headers= headers)
    soup2 = BeautifulSoup(newRESponse.content, 'html.parser')
    
    nAMe = soup2.find('span', class_="hero__primary-text").text
    movie_name.append(nAMe)
    print(movie_name)
    
    MAker = soup2.find('div', class_="ipc-metadata-list-item__content-container").text
    director.append(MAker)
    print(director)
    
    crewMAtes = soup2.find('a', class_="sc-bfec09a1-1 gCQkeh").text
    crew.append(crewMAtes)
    print(crew)
    
    gEN = soup2.find('div', class_="ipc-chip-list__scroller").text
    genere.append(re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', gEN))
    print(genere)
    
        
    story = soup2.find('span', class_="sc-a31b0662-0 iBnSmy").text
    summary.append(story)
    print(summary)
    
    imgs = soup2.find('img', class_="ipc-image")
    image_url.append(imgs['src'])
    print(image_url)
    
    
print("Almost done!")
  
max_length = max(len(movie_name), len(year), len(runtime), len(score), len(votes), len(summary), len(director), len(crew), len(genere))

movie_name += [''] * (max_length - len(movie_name))
year += [''] * (max_length - len(year))
runtime += [''] * (max_length - len(runtime))
score += [''] * (max_length - len(score))
votes += [''] * (max_length - len(votes))
summary += [''] * (max_length - len(summary))
director += [''] * (max_length - len(director))
crew += [''] * (max_length - len(crew))
genere += [''] * (max_length - len(genere))
image_url += [''] * (max_length - len(image_url)) 
    
movie_to = pd.DataFrame({
    "Movie Name": movie_name,
    "Year": year,
    "Run time & Rated": runtime,
    "IMDb-Rating": score,
    "Voting": votes,
    "Summary": summary,
    "Director": director,
    "Starrer": crew,
    "Genere" : genere,
    "Image" : image_url})

movie_to.to_json("movies.json", orient="records", indent=4)

print("scrapping done!")