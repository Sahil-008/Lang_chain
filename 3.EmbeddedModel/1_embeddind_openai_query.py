from langchain import OpenAiEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAiEmbeddings(model='text-embedding-3-large',dimensions =32)#dimensions : size of vector




#result = embedding.embed_query("Delhi is the capital of India")
#
#print(str(result))


documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West bengal",
    "Paris is the capital of France"
]

result = embedding.embed_documents(documents)

print(str(result))