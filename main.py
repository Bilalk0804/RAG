from dotenv import load_dotenv
import os
from langchain_core.prompts  import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.chat_models import init_chat_model
from pydantic import BaseModel

load_dotenv()
llm = init_chat_model("mistralai/mixtral-8x7b-instruct-v0.1", model_provider="Nvidia", api_key=os.getenv("NVIDIA_API_KEY"))
prompt="Tell me about hammer head sharks."
class shark_info(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]
parser=PydanticOutputParser(pydantic_object=shark_info)       
#llm.invoke(prompt)
print(llm.invoke(prompt, parser=PydanticOutputParser))
# for chunks in llm.stream(prompt):
#     print(chunks, end="", flush=True)

