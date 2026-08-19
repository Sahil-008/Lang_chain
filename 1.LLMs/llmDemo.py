from langchain_openai import OpenAI   
from dotenv import load_dotenv  #for the API

load_dotenv() # to invoke

llm = OpenAI(model = 'gpt-3.5-turbo-instruct')

result = llm.invole("Who won the IPL 2025")

print(result)

