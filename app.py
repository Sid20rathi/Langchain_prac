import os
from dotenv import load_dotenv
from langchain_ollama.llms import OllamaLLM
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser



load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"]= os.getenv("LANGCHAIN_PROJECT")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are a helper assistant ,please respond or provide answer in detail to the question asked to u "),
        ("user","Question:{question}")
    ]
)

st.title("Langchain chatbot  demo")
input_text = st.text_input("Enter your question here")

llm = OllamaLLM(model="deepseek-r1")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser
if input_text:
    st.write(chain.invoke({"question": input_text}))