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
        The full content of the file as a string,
        or an error message starting with "Error: ".
    """
    if not os.path.exists(path):
        return "Error: File does not exist"
    if os.path.isdir(path):
        return f"Error: '{path}' is a directory, not a file"
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = file.read()
        return data
    except UnicodeDecodeError:
        return f"Error: File '{path}' is not a valid UTF-8 text file"
    except PermissionError:
        return f"Error: Permission denied to read file '{path}'"
    except OSError as e:
        return f"Error: {e}"