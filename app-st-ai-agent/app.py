import streamlit as st
import json
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.docstore.document import Document
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="Conozcámonos", layout="wide")
st.title("📘 Chat sobre nuestr@s compañer@s")


@st.cache_resource
def setup_rag_chain():
    # Cargar lista de textos desde data.json
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    docs = [Document(page_content=text) for text in data]

    # Separar textos si son largos
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = splitter.split_documents(docs)

    # Crear base vectorial
    embeddings = OpenAIEmbeddings()
    vectordb = FAISS.from_documents(split_docs, embedding=embeddings)

    # Crear cadena de RAG
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})
    llm = ChatOpenAI(temperature=0)
    chain = ConversationalRetrievalChain.from_llm(llm, retriever=retriever)

    return chain

# Inicializar la cadena solo una vez
if "chat_chain" not in st.session_state:
    st.session_state.chat_chain = setup_rag_chain()
    st.session_state.chat_history = []

query = st.chat_input("Haz una pregunta sobre el contenido del archivo JSON...")

if query:
    with st.spinner("Pensando..."):
        response = st.session_state.chat_chain({
            "question": query,
            "chat_history": st.session_state.chat_history
        })
        st.session_state.chat_history.append((query, response["answer"]))

# Mostrar historial de conversación
for i, (q, a) in enumerate(st.session_state.chat_history):
    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(q)
    with st.chat_message("assistant", avatar="🤖"):
        st.markdown(a)
