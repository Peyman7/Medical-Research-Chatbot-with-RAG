
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

## Setup

1. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

2. Add your API keys:
   - Copy `.env.example` to `.env`
   - Insert your OpenAI and SerpAPI keys:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     SERPAPI_API_KEY=your_serpapi_api_key_here
     ```

3. Run the notebook and interact with the chatbot.

## Usage

- Modify the `query` variable to target your research topic of interest.
- The chatbot will retrieve, embed, and respond based on summarized content.


