'''First I will work with domo basic langchain templates and then I will move on to the project'''
#TASK::
'''Sentiment analysis: ascertain whether the overall sentiment of a given piece of text is 'positive' or 'negative'.
Main topic identification: identify and state the main topic for a given piece of text.
Followup question generation: generate an appropriate and interesting followup question that will clarify some aspect of a given piece of text.'''
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import PromptTemplate
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from dotenv import load_dotenv
import os
load_dotenv()
#available_models = ChatNVIDIA.get_available_models()
#print("Available models:", available_models[0])
llm=ChatNVIDIA(
    model="meta/llama-3.1-8b-instruct",
    api_key=os.getenv("NVIDIA_API_KEY"),
    temperature=0.0
)
# prompt="who are you?"
# print(llm.invoke(prompt).content)
english_to_spanish_template = ChatPromptTemplate.from_template("""Translate the following from English to Italian. \
Provide only the translated text: '{english_statement}'""")
prompt = english_to_spanish_template.invoke({"english_statement": "Today is a good day."})

print(llm.invoke(prompt).content)
statements = [
    "I had a fantastic time hiking up the mountain yesterday.",
    "The new restaurant downtown serves delicious vegetarian dishes.",
    "I am feeling quite stressed about the upcoming project deadline.",
    "Watching the sunset at the beach was a calming experience.",
    "I recently started reading a fascinating book about space exploration."
]
