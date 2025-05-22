const express = require('express');
const axios = require('axios');
require('dotenv').config();

const app = express();
const togetherAI = axios.create({
  baseURL: 'https://api.together.xyz/v1',
  headers: {
    Authorization: `Bearer ${process.env.TOGETHER_AI_API_KEY}`,
    'Content-Type': 'application/json'
  }
});

// Configuration
app.set('view engine', 'ejs');
app.use(express.static('public'));
app.use(express.json());

// SEO-optimized main route
app.get('/', (req, res) => {
  res.render('index', {
    title: 'AI Chatbox',
    description: 'An intelligent chat interface powered by Together AI'
  });
});

// API Test Endpoint
app.get('/test-api', async (req, res) => {
  try {
    const response = await togetherAI.post('/chat/completions', {
      model: 'meta-llama/Llama-3-8b-chat-hf',
      messages: [{ role: 'user', content: "Say 'API connection successful'" }],
      max_tokens: 50
    });
    res.send(response.data.choices[0].message.content);
  } catch (error) {
    res.status(500).send(`API Error: ${error.message}`);
  }
});

// Chat Endpoint with Enhanced Error Handling
app.post('/chat', async (req, res) => {
  try {
    if (!req.body.message?.trim()) {
      throw new Error('Empty message received');
    }

    const response = await togetherAI.post('/chat/completions', {
      model: 'meta-llama/Llama-3-8b-chat-hf',
      messages: [{ role: 'user', content: req.body.message }],
      max_tokens: 500
    });

    const responseText = response.data.choices[0].message.content;

    if (!responseText) {
      throw new Error('Received empty response from API');
    }

    res.json({ response: responseText });
    
  } catch (error) {
    console.error('Server Error:', error);
    res.status(500).json({
      error: error.message.includes('API key') 
        ? 'Invalid API configuration' 
        : error.message
    });
  }
});

app.listen(process.env.PORT, () => {
  console.log(`Server running on port ${process.env.PORT}`);
});