from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructureOutputParser, ResponseSchema
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id ="TinyLlama/TinyLlama-1-1b-chat-v1.0",
    task = "text-generation",
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name="name", description="the name of the fictional character"), 
    ResponseSchema(name="age", description="the age of the fictional character"),
    ResponseSchema(name="city", description="the city of the fictional character")
]

parser = StructureOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template ='give me the name, age and city of a fictional character \n {format}',
    input_variables = [],
    partial_variables = {'format':parser.get_format_instructions()}
)

#prompt = template.invoke({})
#
#result = model.invoke(prompt)
#
#final_result = parser.parse(result.content)
#
#print(final_result)

chain = template | model | parser #it will help to get the content from the result in parser and send it to next template and model, without making new chain for each step

result = chain.invoke()

print(result)

#no data validation