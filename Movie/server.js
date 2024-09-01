const express = require("express");
const app = express();
const path = require("path");
const hbs = require("hbs");
const collection = require("./mongodb");
const fs = require('fs');

const templatePath = path.join(__dirname, '../public');

app.use(express.static('public'));

app.use(express.json());
app.set('view engine', 'hbs');
app.set('views', templatePath);
app.use(express.urlencoded({ extended: false }));

const moviesData = JSON.parse(fs.readFileSync(path.resolve(__dirname, 'movies.json'), 'utf8'));

app.get("/", (req, res) => {
    res.render('login');
});

app.get('/signup', (req, res) => {
    res.render('signup');
});

app.post('/signup', async (req, res) => {
    const data = {
        name: req.body.name,
        password: req.body.password
    };

    await collection.insertMany([data]);
    res.render('index');
});

app.post('/login', async (req, res) => {
    
    try{
        const check=await collection.findOne({name:req.body.name});

        if(check.password===req.body.password){
            res.render('index');
        }

        else{
            res.send("Invalid! Please enter correct password");
        }
    }

    catch{
        res.send("Invalid username or password")
    }
    
});

app.get('/movies', (req, res) => {
  res.json(moviesData);
});

app.get('/movies/search', (req, res) => {
  const query = req.query.q.toLowerCase().trim();
  const filteredMovies = moviesData.filter(movie =>
    movie.Movie_Name.toLowerCase().includes(query) ||
    movie.Summary.toLowerCase().includes(query) ||
    movie.Director.toLowerCase().includes(query) ||
    movie.Genere.toLowerCase().includes(query)
  );
  res.json(filteredMovies);
});

app.listen(5000, () => {
    console.log("Port connection done!");
});