import os
from langchain.tools import tool


@tool
def makedir(path: str) -> str:
    os.mkdir(path)
    return "ok"
