from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage

from dotenv import load_dotenv
import os
load_dotenv()
# models=ChatNVIDIA.get_available_models()
# print("Available models:", models[1])
llm=ChatNVIDIA(
    model="meta/llama-3.1-8b-instruct",
    api_key=os.getenv("NVIDIA_API_KEY"),    
)
prompt="what is the capital of Ethiopia?"
print(llm.invoke(prompt).content)
prompt_template = ChatPromptTemplate.from_template("{prompt}")
chain = prompt_template | llm
# Provide the required input to the chain
print(chain.invoke({"prompt": "hello"}))
# prompt_result = prompt_template.invoke({"prompt": "hello"})
# print(prompt_result)
'''assigining a human role remmenber in new version using this[] already includes .from_messages()'''
template=ChatPromptTemplate.from_messages(["Give the concise etomology of the following English word: {word}"])
parcer=StrOutputParser()
chain=template | llm | parcer   
print(chain.invoke({"word":"lament"}))
'''we can give ai roles as well like this'''

prompt_template = ChatPromptTemplate.from_messages([
    ("human", "Hello."),
    ("ai", "Hello, how are you?"),
    ("human", "{prompt}")
])
'''both can be used interchangeably but the first one is more readable'''
prompt_template = ChatPromptTemplate.from_messages([
    HumanMessage(content="Hello"),
    AIMessage(content="Hello, how are you?"),
    HumanMessage(content="{prompt}")
])
prompt = prompt_template.invoke({"prompt": "I'm well, thanks!"})
prompt.to_messages()

#few short prompting also known as 1,2, many shot prompting
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
city_info_prompt_template = ChatPromptTemplate.from_messages([
    # few_shot_prompt, # NOTE: we would like to provide several examples here in the form of a few-shot prompt.
    ("human", "Provide information about the following city in exactly the same format as you've done in previous responses: City: {city}")
])
city_examples_location = [
    {"city": "Oakland", "output": "Oakland, USA, North America, Earth"},
    {"city": "Paris", "output": "Paris, France, Europe, Earth"},
    {"city": "Lima", "output": "Lima, Peru, South America, Earth"},
    {"city": "Seoul", "output": "Seoul, South Korea, Asia, Earth"}
]
prompt_template_for_examples = ChatPromptTemplate.from_messages([
    ("human", "{city}"),
    ("ai", "{output}"),
])

'''system messages are used to set the behavior of the model'''

prompt_template = ChatPromptTemplate([
    ("system", "You are a pirate. Your name is Sam. You always talk like a pirate"),
    ("human", "{prompt}")
])
parser = StrOutputParser()
chain = prompt_template | llm | parser
chain.invoke({"prompt": "Who are you?"})

"""chain of thought prompting"""
'''Chain of thought prompting is a technique where the model is encouraged to think step by step before arriving at a final answer. This can be particularly useful for complex reasoning tasks.'''
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
'''Few shot prompting is a technique where the model is provided with a few examples of the task at hand to help it understand the context and expected output.'''
example_problem = 'What is 678 * 789?'
example_cot = '''\
Let me break this down into steps. First I'll break down 789 into hundreds, tens, and ones:

789 -> 700 + 80 + 9

Next I'll multiply 678 by each of these values, storing the intermediate results:

678 * 700 -> 678 * 7 * 100 -> 4746 * 100 -> 474600

My first intermediate result is 474600.

678 * 80 -> 678 * 8 * 10 -> 5424 * 10 -> 54240

My second intermediate result is 54240.

678 * 9 -> 6102

My third intermediate result is 6102.

My three intermediate results are 474600, 54240, and 6102.

Adding the first two intermediate results I get 474600 + 54240 -> 528840.

Adding 528840 to the last intermediate result I get 528840 + 6102 -> 534942

The final result is 534942.
'''
multiplication_template = ChatPromptTemplate.from_messages([
    ('human', example_problem),
    ('ai', example_cot),
    ('human', '{long_multiplication_prompt}')
])
multiplication_chain = multiplication_template | llm | StrOutputParser()
print(multiplication_chain.invoke({'long_multiplication_prompt': 'What is 345 * 888?'}))