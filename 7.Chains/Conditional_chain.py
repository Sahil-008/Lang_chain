from langchain_core.runnables import RunnableBranch, chain
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableParallel, runnableBranch
from pydantic import BaseModel, Field   
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

model1 = ChatAnthropic(model_name="claude-3")

parser = StrOutputParser()

class Feedback(baseModel):
    sentiment: Literal["positive", "negative", "neutral"] = field(description="The sentiment of the feedback text, which can be positive, negative, or neutral.")

parser2 = PydanticOutputParser(pydantic_object=Feedback)
prompt1 = PromptTemplate(
    template = 'Classify the sentiment of the following feedback text into positive, negative, or neutral: \n {text}',
    input_variables = ['text'],
)

prompt2 = PromptTemplate(
    template = 'Generate a summary of the following feedback text: \n {text} \n {format_instructions}',
    input_variables = ['text'],
    partial_variables = {'format_instructions': parser2.get_format_instructions()}
)

classification_chain = prompt1 | model1 | parser2

result = classification_chain.invoke({"text": "I love this product! It has exceeded my expectations."}).sentiment

print(f"Sentiment classification result: {result}")


prompt3 = PromptTemplate(
    template = 'Write a appropriate response to this positive feedback: \n {text}',
    input_variables = ['text'],
)

prompt4 = PromptTemplate(
    template = 'Write a appropriate response to this negative feedback: \n {text}', 
    input_variables = ['text'],
)

prompt5 = PromptTemplate(
    template = 'Write a appropriate response to this neutral feedback: \n {text}',

    input_variables = ['text'],
)


classification_chain = prompt1 | model1 | parser2



branch_chain = RunnableBranch(
    lambda inputs: inputs["sentiment"],
    {
        "positive": prompt3 | model1 | parser,
        "negative": prompt4 | model1 | parser,
        "neutral": prompt5 | model1 | parser,
    },
)