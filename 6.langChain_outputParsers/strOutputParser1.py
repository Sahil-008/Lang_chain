from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id ="TinyLlama/TinyLlama-1-1b-chat-v1.0",
    task = "text-generation",
)

model = ChatHuggingFace(llm=llm)

#detailed report

template1 = PromptTemplate(
    template ='write a detailed report on the following topic: {topic}',
    input_variables = ['topic']
)

#summy report

template2 = PromptTemplate(
    template ='write a summary report on the following topic: {topic}',
    input_variables = ['topic']
)

parser = StrOutputParser()

chain = template1  | model | parser | template2 | model | parser

chain.invoke({'topic':'Climate Change'})