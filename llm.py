# llm.py
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

print(os.getenv("API_KEY"))

llm = ChatOpenAI(
    model="qwen/qwen3.5-plus-20260420",   # или "gpt-3.5-turbo"
    temperature=0.8,
    api_key=os.getenv("API_KEY"), # API-ключ из переменной окружения
    base_url="https://openrouter.ai/api/v1"
)

# response = llm.invoke([HumanMessage(content="Hello, how are you?")])
# print(response.content)