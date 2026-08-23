from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header('Reasearch Tool')
model = ChatOpenAI(model ='gpt-4')
user_input = st.text_input('Enter Your Prompt')#static prompt where user gave the whole prompt
#dynamic prompt where we gave some option to user to chose 

if st.button('Summarize'):
    result = model.invoke(user_input)
    print(result.content)

    