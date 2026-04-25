import os
import streamlit as st
import ollama

os.environ["USER_AGENT"] = "local-rag-app/1.0"

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

st.title("Chat with Webpage 🌐")
st.caption("This app allows you to chat with a webpage using local TinyLlama and RAG")

webpage_url = st.text_input("Enter Webpage URL", type="default")

rag_ready = False

if webpage_url:
    with st.spinner("Chargement de la page et création de l'index..."):
        loader = WebBaseLoader(webpage_url)
        docs = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=10
        )
        splits = text_splitter.split_documents(docs)

        embeddings = OllamaEmbeddings(model="nomic-embed-text")

        vectorstore = Chroma.from_documents(
            documents=splits,
            embedding=embeddings
        )

        retriever = vectorstore.as_retriever()
        rag_ready = True

    st.success(f"Loaded {webpage_url} successfully!")

def ollama_llm(question, context):
    formatted_prompt = f"""
Answer the question using only the context below.

Question:
{question}

Context:
{context}
"""

    response = ollama.chat(
        model="tinyllama",
        messages=[
            {"role": "user", "content": formatted_prompt}
        ]
    )

    return response["message"]["content"]

def combine_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

prompt = st.text_input("Ask any question about the webpage")

if prompt:
    if not webpage_url:
        st.warning("Entre d'abord une URL de page web.")
    elif not rag_ready:
        st.warning("La page n'est pas encore prête.")
    else:
        retrieved_docs = retriever.invoke(prompt)
        formatted_context = combine_docs(retrieved_docs)
        result = ollama_llm(prompt, formatted_context)
        st.write(result)