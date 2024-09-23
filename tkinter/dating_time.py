import tkinter as tk
from tkinter import messagebox
import json
import os
import random

FILENAME = "store.json"

def load_profiles():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    else:
        return []

def save_profiles(profiles):
    with open(FILENAME, "w") as file:
        json.dump(profiles, file, indent=4)

def create_profile():
    name = entry_name.get()
    age = entry_age.get()
    bio = entry_bio.get("1.0", "end-1c")
    gender = gender_var.get()

    if not name or not age or not bio or gender == "Select Gender":
        messagebox.showwarning("Input Error", "All fields must be filled!")
        return

    profiles = load_profiles()
    new_profile = {"name": name, "age": age, "bio": bio, "gender": gender}
    profiles.append(new_profile)
    save_profiles(profiles)

    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_bio.delete("1.0", tk.END)
    gender_var.set("Select Gender")

    messagebox.showinfo("Profile Created", "Profile successfully created!")

def view_matches():
    profiles = load_profiles()
    
    if not profiles:
        messagebox.showinfo("No Profiles", "No profiles found!")
        return
    
    males = [p for p in profiles if p["gender"] == "Male"]
    females = [p for p in profiles if p["gender"] == "Female"]

    if not males or not females:
        messagebox.showinfo("No Matches", "Not enough profiles to create matches!")
        return
    
    random.shuffle(males)
    random.shuffle(females)
    
    matches_text = ""
    max_matches = min(len(males), len(females))
    
    for i in range(max_matches):
        male = males[i]
        female = females[i]
        matches_text += f"Match {i+1}:\nMale: {male['name']} (Age: {male['age']})\nFemale: {female['name']} (Age: {female['age']})\n\n"

    # Also display female-to-male matches (reverse pairing)
    random.shuffle(males)
    random.shuffle(females)
    
    for i in range(max_matches):
        female = females[i]
        male = males[i]
        matches_text += f"Match {i+1} (Reverse):\nFemale: {female['name']} (Age: {female['age']})\nMale: {male['name']} (Age: {male['age']})\n\n"
    
    messagebox.showinfo("Random Matches", matches_text)

app = tk.Tk()
app.title("Simple Dating App")
app.geometry("400x450")

label_title = tk.Label(app, text="Create a Profile", font=("Arial", 16))
label_title.pack(pady=10)

label_name = tk.Label(app, text="Name")
label_name.pack()

entry_name = tk.Entry(app, width=30)
entry_name.pack()

label_age = tk.Label(app, text="Age")
label_age.pack()

entry_age = tk.Entry(app, width=30)
entry_age.pack()

label_gender = tk.Label(app, text="Gender")
label_gender.pack()

gender_var = tk.StringVar(app)
gender_var.set("Select Gender")

gender_menu = tk.OptionMenu(app, gender_var, "Male", "Female")
gender_menu.pack()

label_bio = tk.Label(app, text="Bio")
label_bio.pack()

entry_bio = tk.Text(app, width=30, height=5)
entry_bio.pack()

button_create = tk.Button(app, text="Create Profile", command=create_profile, width=20)
button_create.pack(pady=10)

button_view = tk.Button(app, text="View Random Matches", command=view_matches, width=20)
button_view.pack(pady=10)

app.mainloop()
