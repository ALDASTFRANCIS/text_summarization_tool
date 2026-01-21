Text summarization tool that runs as a browser extension. It allows users to summarize news articles and blog posts without clicking the link. It uses a Python backend running a T5 Transformer model to process text and a Chrome Extension to display the results.

Project Architecture

  1.Frontend (Chrome Extension): Injects a UI button next to links. It communicates with the backend via a background service worker to avoid CORS/Mixed       Content issues.
  
  2.Backend (FastAPI): Receives a URL, scrapes the article content, and feeds it into a Machine Learning model.

  3.ML Model (Hugging Face): Uses t5-small to generate an abstractive summary of the scraped text.

Prerequisites

  -Python 3.8 or higher
  
  -Google Chrome (or Chromium-based browser like Brave/Edge)# text_summarization_tool
