import os
from langchain.tools import tool


@tool
def listdir(path: str) -> str:
    return ",".join(os.listdir(path))
