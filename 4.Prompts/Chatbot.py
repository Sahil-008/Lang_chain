from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

chat_history = []

while True:
    user_input = input('You : ')
    chat_history.append(user_input)
    if user_input == 'exit' :
        break
    result = model.invoke(chat_history)
    chat_history.append(result)
    print("AI: ",result.content) #no context stored now, so AI can remember out chat for that use chat_history

print(chat_history)