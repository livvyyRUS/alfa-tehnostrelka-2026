from langchain.tools import tool


@tool
def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as file:
        data = file.read()
    return data
