import os
from langchain.tools import tool
from .security import check_path

@tool
def write_file(path: str, data: str) -> str:
    """
    Write text data to a file (overwrites if exists).

    Use this tool when you need to create or update a file.
    All paths are relative to the 'output' directory or must be within it.

    Args:
        path: Relative or absolute path to the file (must be inside 'output').
        data: Text content to write into the file.

    Returns:
        "ok" if the file was successfully written,
        or an error message starting with "Error: ".
    """
    try:
        safe_path = check_path(path)

        # Проверим, не пытаемся ли мы писать в директорию
        if os.path.exists(safe_path) and os.path.isdir(safe_path):
            return f"Error: '{path}' is a directory, cannot write as a file"

        with open(safe_path, "w", encoding="utf-8") as file:
            file.write(data)
        return "ok"

    except PermissionError as e:
        return f"Error: {e}"
    except OSError as e:
        return f"Error: {e}"