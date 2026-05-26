from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_nvidia_ai_endpoints import ChatNVIDIA


load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


GROQ_API_KEY = os.getenv("GROQ_API_KEY")
NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")

# llm = ChatNVIDIA(
#   model="minimaxai/minimax-m2.7",
#   api_key=NVIDIA_API_KEY, 
#   temperature=1,
#   top_p=0.7,
#   max_tokens=4096,
# )

# for chunk in llm.stream([{"role":"user","content":"How many 'r's are in 'strawberry'?"}]):
#   print(chunk.content, end="")


# llm = ChatOpenAI(
#     model="gpt-4o-mini",
#     temperature=0.3
# )


llm = ChatGroq(
    model="llama-3.3-70b-versatile",  # or "llama3-70b-8k"
    api_key=GROQ_API_KEY
)


