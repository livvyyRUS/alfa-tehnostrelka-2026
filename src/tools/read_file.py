import os
from langchain.tools import tool


@tool
def read_file(path: str) -> str:
    """
    Read the contents of a text file.

    Use this tool when you need to access or analyze file contents.

    Args:
        path: Path to the file.

    Returns:
        The full content of the file as a string.
    """
    if not os.path.exists(path):
        return "Not exists"
    with open(path, "r", encoding="utf-8") as file:
        data = file.read()
    return data
