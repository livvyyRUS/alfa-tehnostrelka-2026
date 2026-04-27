from langchain.tools import tool

@tool
def write_file(path: str, data: str) -> str:
    """Получить погоду в городе"""
    with open(path, "w", encoding="utf-8") as file:
        file.write(data)
    return "ok"