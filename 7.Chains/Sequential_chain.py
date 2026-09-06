from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template ="Genrate a detailed report on {topic}.",
    input_variables=["topic"],
)

prompt2 = PromptTemplate(
    template ="Genrate 5 important points from the following text: \n {text}.",
    input_variables=["text"],
)


model = ChatOpenAI()

parser = StrOutputParser()

chain = prompt | model | parser | prompt2 | model | parser

result =chain.invoke({"topic": "space exploration"})

print(result)

print(chain.get_graph().print_ascii()) # to see the chain structure in ascii format