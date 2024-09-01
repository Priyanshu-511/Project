const mongoose = require("mongoose");

mongoose.connect("mongodb://localhost:27017/movieMAnia")
    .then(() => {
        console.log("MongoDB connected successfully");
    })
    .catch((error) => { 
        console.error("MongoDB connection failed:", error);
    });

const loginSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true
    },
    password: {
        type: String,
        required: true
    }
});

const collection = mongoose.model("collection1", loginSchema);

module.exports = collection;
