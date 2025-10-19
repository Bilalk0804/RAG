from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os
'''langchain is so much better for working with this can literallt call any model with just a few lines of code'''
client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = os.getenv("NVIDIA_API_KEY"),
)

completion = client.chat.completions.create(
  model="meta/llama-3.1-8b-instruct",
  messages=[{"role":"user","content":"Tell me about openai API."}],
  temperature=0.2,
  top_p=0.7,
  max_tokens=512,
  stream=True
)

for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")