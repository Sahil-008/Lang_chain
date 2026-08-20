from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv


load_dotenv()

model = ChatAnthropic(mmodel = 'claude-3-5', temperature=1.4)

result = model.invoke("who is  kholi")

print(result.content)