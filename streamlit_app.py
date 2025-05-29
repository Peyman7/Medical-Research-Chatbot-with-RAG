import os
import streamlit as st
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, ServiceContext
from llama_index.embeddings.openai import OpenAIEmbedding
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain_community.vectorstores.faiss import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.memory import ConversationSummaryBufferMemory
from langchain.schema import Document
import arxiv
import requests
from bs4 import BeautifulSoup
from serpapi import GoogleSearch

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
serpapi_key = os.getenv("SERPAPI_API_KEY")

# === Utility Functions ===
def fetch_arxiv_papers(query, max_results=3):
    client = arxiv.Client()
    search = arxiv.Search(query=query, max_results=max_results, sort_by=arxiv.SortCriterion.SubmittedDate)
    results = client.results(search)
    return [{"title": result.title, "summary": result.summary, "source": "arXiv"} for result in results]

def get_pubmed_abstract(pmid):
    url = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    content = soup.find("div", class_="abstract-content")
    return content.text.strip() if content else "Abstract not found"

def fetch_pubmed_papers(query, max_results=3):
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {"db": "pubmed", "term": query, "retmode": "json", "retmax": max_results}
    pmids = requests.get(search_url, params=params).json()['esearchresult']['idlist']
    return [{"title": f"PubMed article {pmid}", "summary": get_pubmed_abstract(pmid), "source": "PubMed"} for pmid in pmids]

def get_scholar_details(url):
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find("h3", class_="gs_rt")
    abstract = soup.find("div", class_="gs_rs")
    return {"title": title.text.strip() if title else "Title not found", "summary": abstract.text.strip() if abstract else "Abstract not found"}

def search_google_scholar(query, max_results=3):
    params = {"q": query, "api_key": serpapi_key, "engine": "google_scholar", "num": max_results}
    search = GoogleSearch(params)
    results = search.get_dict().get("organic_results", [])
    papers = []
    for r in results:
        url = r.get("link")
        details = get_scholar_details(url) if url else {"title": r["title"], "summary": "No abstract"}
        papers.append({"title": details["title"], "summary": details["summary"], "source": "Google Scholar"})
    return papers

def process_papers(papers, max_words=150):
    docs = []
    for paper in papers:
        text = f"Title: {paper['title']}\nAbstract: {paper['summary']}\nSource: {paper['source']}"
        trimmed = " ".join(text.split()[:max_words])
        docs.append(Document(page_content=trimmed, metadata={"title": paper["title"], "source": paper["source"]}))
    return docs

# === Streamlit UI ===
st.title("🧠 Medical Research Chatbot (RAG)")
query = st.text_input("Enter your medical research topic:", placeholder="e.g., Sleep and Memory Consolidation")

if query:
    with st.spinner("🔍 Fetching papers..."):
        papers = fetch_arxiv_papers(query) + fetch_pubmed_papers(query) + search_google_scholar(query)
        documents = process_papers(papers)

        vectorstore = FAISS.from_documents(documents, OpenAIEmbeddings(openai_api_key=openai_api_key))
        retriever = vectorstore.as_retriever()
        llm = ChatOpenAI(temperature=0, model_name="gpt-4o", openai_api_key=openai_api_key)
        memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=1000, return_messages=True)

        chatbot = ConversationalRetrievalChain.from_llm(llm=llm, retriever=retriever, memory=memory)

    st.success("✅ Ready! Start chatting with the bot below.")
    user_question = st.text_input("Ask a question about the papers:")

    if user_question:
        response = chatbot.run(user_question)
        st.markdown(f"**Answer:** {response}")