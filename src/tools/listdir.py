import os
from langchain.tools import tool


@tool
def listdir(path: str) -> str:
    """
    List files and directories inside a given folder.

    Use this tool when you need to inspect the contents of a directory.

    Args:
        path: Absolute or relative path to the directory.

    Returns:
        A comma-separated string of file and directory names,
        or an error message starting with "Error: ".
    """
    try:
        if not os.path.exists(path):
            return "Error: Path does not exist"
        return ",".join(os.listdir(path))
    except NotADirectoryError:
        return f"Error: '{path}' is not a directory"
    except PermissionError:
        return f"Error: Permission denied to read directory '{path}'"
    except OSError as e:
        return f"Error: {e}"