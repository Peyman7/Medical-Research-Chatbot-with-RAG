
# Medical Research Chatbot with RAG

This project implements a Retrieval-Augmented Generation (RAG) chatbot that assists users in exploring and understanding medical research papers. It retrieves relevant documents from arXiv, PubMed, and Google Scholar, summarizes them using GPT-4, and enables interactive question answering.

## Features

- Fetches medical papers from arXiv, PubMed, and Google Scholar
- Summarizes abstracts using OpenAI's GPT-4
- Builds a chatbot using LangChain with FAISS vector storage
- Uses `ConversationSummaryBufferMemory` for context retention

## Technologies Used

- Python
- LangChain
- OpenAI API (GPT-4, Embeddings)
- FAISS
- arXiv and PubMed APIs
- Google Scholar via SerpAPI
- Web scraping via BeautifulSoup

## ⚙️ Setup

### 1. Clone and Configure
```bash
cp .env.example .env
# Add your OpenAI and SerpAPI keys to the .env file
```

### 2. Run with Docker
```bash
docker build -t medagent .
docker run -p 8501:8501 --env-file .env medagent
```

Or use Docker Compose:
```bash
docker-compose up --build
```

### 3. Run Locally
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## 📄 .env File Example
```
OPENAI_API_KEY=your_openai_api_key
SERPAPI_API_KEY=your_serpapi_api_key
```

## Usage

- Modify the `query` variable to target your research topic of interest.
- The chatbot will retrieve, embed, and respond based on summarized content.


