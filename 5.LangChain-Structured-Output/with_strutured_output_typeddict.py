from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatOpenAI()

# Schema
class Review(TypedDict):
    summary :str
    sentiment : str

structured_model = model.with_strutured_output(Review)


result = model.invoke(""" The Redmi Note 12 Pro offers a beautiful display, smooth performance, good cameras, and fast charging at a reasonable price.
Overall, it’s a reliable and stylish phone that delivers great value for everyday use.
""")

print(result)
print(result['summary'])
print(result['sentiment'])

# to get a specific output like for pros want one key, for cons want other, you can get it by Annotated 
# no data validation, result may or may not follow your data type you want in output