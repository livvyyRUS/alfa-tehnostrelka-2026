import os
from langchain.tools import tool
from .security import check_path

@tool
def read_file(path: str) -> str:
    """
    Read the contents of a text file.

    Use this tool when you need to access or analyze file contents.
    All paths are relative to the 'output' directory or must be within it.

    Args:
        path: Relative or absolute path to the file (must be inside 'output').

    Returns:
        The full content of the file as a string,
        or an error message starting with "Error: ".
    """
    try:
        safe_path = check_path(path)

        if not os.path.exists(safe_path):
            return "Error: File does not exist"
        if os.path.isdir(safe_path):
            return f"Error: '{path}' is a directory, not a file"

        with open(safe_path, "r", encoding="utf-8") as file:
            data = file.read()
        return data

    except PermissionError as e:
        return f"Error: {e}"
    except UnicodeDecodeError:
        return f"Error: File '{path}' is not a valid UTF-8 text file"
    except OSError as e:
        return f"Error: {e}"