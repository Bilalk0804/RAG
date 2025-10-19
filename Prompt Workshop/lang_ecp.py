from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os
load_dotenv()
client = ChatNVIDIA(
  model="meta/llama-3.1-8b-instruct",
  api_key=os.getenv("NVIDIA_API_KEY"),
  temperature=0.0
)
#normal prompt method will forst generate the whole output then print it
prompt='when is capital of africa'
result=client.invoke(prompt)
print(result.content)
#this method is used when when you want to print the output in chunks like wordby word
for chunk in client.stream(prompt):
   print(chunk.content, end='')
for chunk in client.stream([{"role":"user","content":"Write a limerick about the wonders of GPU computing."}]): 
  print(chunk.content, end="")

  #for passing multiple questions in batch use this method

# Process multiple questions one by one
for question in [
    'What is the capital of California?',
    'What is the capital of Texas?',
    'What is the capital of New York?',
    'What is the capital of Florida?',
    'What is the capital of Illinois?',
    'What is the capital of Ohio?'
]:
    result = client.invoke(question)
    print(f"Question: {question}")
    print(f"Answer: {result.content}\n")


##FAQ function
# faq_questions = [
#     'What is a Large Language Model (LLM)?',
#     'How do LLMs work?',
#     'What are some common applications of LLMs?',
#     'What is fine-tuning in the context of LLMs?',
#     'How do LLMs handle context?',
#     'What are some limitations of LLMs?',
#     'How do LLMs generate text?',
#     'What is the importance of prompt engineering in LLMs?',
#     'How can LLMs be used in chatbots?',
#     'What are some ethical considerations when using LLMs?'
# ]
# faq_answers = llm.batch(faq_questions)
# def create_faq_document(faq_questions, faq_answers):
#     faq_document = ''
#     for question, response in zip(faq_questions, faq_answers):
#         faq_document += f'{question.upper()}\n\n'
#         faq_document += f'{response.content}\n\n'
#         faq_document += '-'*30 + '\n\n'

#     return faq_document


'''prompt Template'''
english_to_spanish_template = ChatPromptTemplate.from_template("""Translate the following from English to Italian. \
Provide only the translated text: '{english_statement}'""")
prompt = english_to_spanish_template.invoke({"english_statement": "Today is a good day."})
'''while template call we just need to pass the input in the form of dictionary'''
