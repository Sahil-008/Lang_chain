from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header('Reasearch Tool')

user_input = st.text_input('Enter Your Prompt')

if st.button('Summarize'):
    result = model.invoke(user_input)
    print(result.content)

    