from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model ='gpt-4')# parameter : temperature =) control the randomness of a language of the model's output (range 0:2)


result = model.invoke("Who won world cup 2023")
# result has content plus meta data too
# to get only content use result.content

print(result)