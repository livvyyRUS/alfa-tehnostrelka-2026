import os
from langchain.tools import tool

@tool
def listdir(path: str) -> str:
    """Получить погоду в городе"""
    return ",".join(os.listdir(path))