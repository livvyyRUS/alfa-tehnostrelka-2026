import os
from langchain.tools import tool
from .security import check_path

@tool
def listdir(path: str) -> str:
    """
    List files and directories inside a given folder.

    Use this tool when you need to inspect the contents of a directory.
    All paths are relative to the 'output' directory or must be within it.

    Args:
        path: Relative or absolute path to the directory (must be inside 'output').

    Returns:
        A comma-separated string of file and directory names,
        or an error message starting with "Error: ".
    """
    try:
        safe_path = check_path(path)
        if not os.path.exists(safe_path):
            return "Error: Path does not exist"
        if not os.path.isdir(safe_path):
            return f"Error: '{path}' is not a directory"
        return ",".join(os.listdir(safe_path))
    except PermissionError as e:
        return f"Error: {e}"
    except OSError as e:
        return f"Error: {e}"