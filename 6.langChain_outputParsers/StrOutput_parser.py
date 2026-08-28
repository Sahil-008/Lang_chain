from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
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

prompt1 = template1.invoke({'topic':'Climate Change'})

result1 = model.invoke(prompt1)

prompt2 = template2.invoke({'topic':'Climate Change'})

result2 = model.invoke(prompt2)

print(result1.content)
