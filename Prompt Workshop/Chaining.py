'''Chaining is by fat the most interesting topic I have seen like it gives me the flexibility to even 
choose which model I would like to run and How exactly just by using a simple |.'''
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from dotenv import load_dotenv
import os
load_dotenv()
models=ChatNVIDIA.get_available_models()
print("Available models:", models[1])
llm=ChatNVIDIA(
    model="meta/llama-3.1-8b-instruct",
    api_key=os.getenv("NVIDIA_API_KEY"),    
)
prompt="what is the capital of Ethiopia?"
print(llm.invoke(prompt).content)
#Model is working fine
#I will now try to use the chaining method
