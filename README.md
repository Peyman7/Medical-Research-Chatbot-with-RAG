
# Medical Research Chatbot with RAG

This project implements a Retrieval-Augmented Generation (RAG) chatbot that assists users in exploring and understanding medical research papers. It retrieves relevant documents from arXiv, PubMed, and Google Scholar, summarizes them using GPT-4, and enables interactive question answering.

## Features

- 🔍 Fetches medical papers from arXiv, PubMed, and Google Scholar
- 🧠 Summarizes abstracts using OpenAI's GPT-4
- 🤖 Builds a chatbot using LangChain with FAISS vector storage
- 🗂️ Uses `ConversationSummaryBufferMemory` for context retention

## Technologies Used

- Python
- LangChain
- OpenAI API (GPT-4, Embeddings)
- FAISS
- arXiv and PubMed APIs
- Google Scholar via SerpAPI

## Setup

1. Install required packages:
   ```bash
   pip install llama-index openai langchain langchain_community langchain-openai faiss-cpu arxiv serpapi google-search-results requests beautifulsoup4 streamlit
   ```

2. Set API keys securely (e.g., in environment variables or notebook cell):
   - `OPENAI_API_KEY`
   - `SERPAPI_API_KEY`

3. Run the notebook and interact with the chatbot.

## Usage

- Modify the `query` variable to target your research topic of interest.
- The chatbot will retrieve, embed, and respond based on summarized content.

## Author

Developed by [Your Name], powered by LangChain and OpenAI.
