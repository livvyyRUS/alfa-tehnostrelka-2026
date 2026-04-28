import os
import shutil
from langchain.tools import tool


@tool
def remove_path(path: str) -> str:
    """
    Remove a file or directory at the given path.

    Use this tool when you need to delete a file or an entire directory.

    Args:
        path: Absolute or relative path to the file or directory.

    Returns:
        A success message or an error message starting with "Error: ".
    """
    try:
        if not os.path.exists(path):
            return "Error: Path does not exist"

        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
            return f"File '{path}' removed successfully"

        if os.path.isdir(path):
            shutil.rmtree(path)
            return f"Directory '{path}' removed successfully"

        return f"Error: Unknown path type '{path}'"

    except PermissionError:
        return f"Error: Permission denied to remove '{path}'"
    except OSError as e:
        return f"Error: {e}"