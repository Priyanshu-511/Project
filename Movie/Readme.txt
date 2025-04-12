
# 🎬 movieMania Website – Pre-Setup Guide

**Author:** Priyanshu Kumar  
**Date:** April 2024  
**Platform:** 🖥️ Windows  

---

## 📦 1. System & Environment Setup

### Step 1: Install Prerequisites
- Install [Visual Studio Code](https://code.visualstudio.com)
- Install the LTS version of [Node.js](https://nodejs.org)

### Step 2: MongoDB Installation

#### Part 1 – Community Server:
- Download and install **MongoDB Community Server** from the official website.
- Select `Complete` setup type.
- Click `Next` repeatedly and allow permission when prompted.

#### Part 2 – MongoDB Shell:
- Download **MongoDB Shell**
- Extract to:  
  `C:\Program Files\MongoDB`
- Add the following directory to your system **PATH** (Environment Variables):  
  ```
  C:\Program Files\MongoDB\mongosh-2.2.3-win32-x64\bin
  ```

### Step 3: Verify MongoDB Installation
- Open **PowerShell**
- Type:
  ```bash
  mongosh
  ```
- If MongoDB shell starts, the setup is successful.
- Close the terminal.

---

## 🚀 2. Node.js Project Setup

### Step 4: Initialize Node.js App
Open terminal in VS Code (`Ctrl + Shift + ~`) and run:
```bash
npm init
npm i express
npm i hbs
npm i mongoose
npm i nodemon
npm i path
```

### Step 5: Enable Script Execution in PowerShell
- Run PowerShell as Administrator.
- Type:
  ```powershell
  Set-ExecutionPolicy Unrestricted
  ```
- Then type `A` and press `Enter`.

---

## 🧭 3. MongoDB Compass Setup

- Open **MongoDB Compass**
- Use connection URL:
  ```
  mongodb://localhost:27017/
  ```
- Name the connection: `movieMania`
- Click **Save and Connect**

---

## 🛠️ 4. Running the Application

### Step 6: Start the Server
In VS Code terminal:
```bash
nodemon src/index.js
```

### Step 7: Open in Browser
Visit:
```
http://localhost:5000
```

> ⚠️ **If error occurs with MongoDB connection:**  
> Disconnect from Compass and reconnect using the same URL.

---

## 🧪 5. Python Dependencies (Optional)

If you're using Python for additional functionality like scraping:

```bash
python -m pip install flask
python -m pip install bs4
python -m pip install requests
python -m pip install numpy
```

> 🔧 Fix in `movies.json`: Replace every `(\)` with `("\n")` if you face JSON formatting errors.

---

## 💻 6. Extra VS Code Commands

To run the server from a different entry file:
```bash
nodemon src/server.js
```

---

## 🐞 7. Known Issues

- ❌ **MongoDB Data Not Saving**  
  Registration was working earlier, but now it's not saving to MongoDB.

- ❗ **Recommender System Limitation**  
  It only works when the **full movie name** is entered. It's case- and space-sensitive.

---

✅ You're all set! Explore, code, and enhance the **movieMania** experience. 🎥✨
