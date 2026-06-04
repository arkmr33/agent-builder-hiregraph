from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_nvidia_ai_endpoints import ChatNVIDIA

import os
from openai import OpenAI

load_dotenv()

# llm = ChatOpenAI(
#     model="gpt-4o-mini",
#     temperature=0
# )



HF_TOKEN = os.getenv("HF_TOKEN")
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


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    #model="llama-3.1-8b-instant", 
    api_key=GROQ_API_KEY,
    max_tokens=4096,
    temperature=0
)



# llm = OpenAI(
#     base_url="https://router.huggingface.co/v1",
#     api_key=HF_TOKEN,          # ← use the variable here
# )


# llm = client.chat.completions.create(
#     model="openai/gpt-oss-120b:cerebras",
#     messages=[{"role": "user",
#                "content": "How far is moon from the earth?"}],
# )

#print(completion.choices[0].message)

# reply = completion.choices[0].message.content          # the text you really want


# llm = ChatOpenAI(
#     model="openai/gpt-oss-120b:cerebras",
#     base_url="https://router.huggingface.co/v1",
#     api_key=os.getenv("HF_TOKEN"),
#     temperature=0
# )

# response = llm.invoke("How far is the Moon from Earth?")
# print(response.content)



# 1. Get a free token from Hugging Face (Settings -> Access Tokens)
# 2. Set it as an environment variable or paste it directly below
# HF_TOKEN = "your_huggingface_token_here"

# client = OpenAI(
#     base_url="https://huggingface.co", 
#     api_key=HF_TOKEN
# )

# messages = [
#     {"role": "user", "content": "Write a quick sort algorithm."}
# ]

# # This sends a fast network request instead of downloading anything
# completion = client.chat.completions.create(
#     model="Qwen/Qwen3-Coder-480B-A35B-Instruct",
#     messages=messages,
#     max_tokens=500
# )

# print(completion.choices[0].message.content)

# llm = ChatOpenAI(
#     model="Qwen/Qwen3-Coder-480B-A35B-Instruct",
#     base_url="https://router.huggingface.co/v1",
#     api_key=os.getenv("HF_TOKEN"),
#     temperature=0
# )

# response = llm1.invoke("How far is the Moon from Earth?")
# print(response.content)
