import random
class Dummy:
    def __init__(self):
        print("Dummy class initialized")

    def predict(self, input):
       response = [
           'Virat kholi is a former Indian cricketer and captain of the Indian national team. He is widely regarded as one of the greatest batsmen in the history of cricket.',
           'Sachin Tendulkar is a former Indian cricketer and is widely regarded as one of the greatest batsmen in the history of cricket.',
           'Don Bradman is a former Australian cricketer and is widely regarded as one of the greatest batsmen in the history of cricket.'
       ]

       return {'response': random.choice(response)}


class DummyPromptTemplate:
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def format(self, kwargs):
        return self.template.format(**kwargs)


# as of now you have to connect all those classes, first you will give the promth and then call the llm class to get output
#now using chain we can skip that

class DummyChain:
    def __init__(self, prompt_template, llm):
        self.prompt_template = prompt_template
        self.llm = llm

    def run(self, input):
        formatted_prompt = self.prompt_template.format(input)
        return self.llm.predict(formatted_prompt)

template = DummyPromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

llm = Dummy()

chain = DummyChain(template, llm)

chain = chain.run({'topic': 'Virat Kohli'})