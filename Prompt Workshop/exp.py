import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os
#useless without feeding in some money to the api 
client=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.responses.create(
    model="gpt-4o",
    instructions="You are a coding assistant that talks like a pirate.",
    input="How do I check if a Python object is an instance of a class?",
)

print(response.output_text)
