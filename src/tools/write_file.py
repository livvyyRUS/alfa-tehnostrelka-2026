import os
from langchain.tools import tool


@tool
def write_file(path: str, data: str) -> str:
    """
    Write text data to a file (overwrites if exists).

    Use this tool when you need to create or update a file.

    Args:
        path: Path to the file.
        data: Text content to write into the file.

    Returns:
        "ok" if the file was successfully written,
        or an error message starting with "Error: ".
    """
    try:
        # Проверим, не пытаемся ли мы писать в директорию
        if os.path.exists(path) and os.path.isdir(path):
            return f"Error: '{path}' is a directory, cannot write as a file"
        with open(path, "w", encoding="utf-8") as file:
            file.write(data)
        return "ok"
    except PermissionError:
        return f"Error: Permission denied to write file '{path}'"
    except OSError as e:
        return f"Error: {e}"