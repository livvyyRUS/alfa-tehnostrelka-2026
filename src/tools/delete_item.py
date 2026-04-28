import os
import shutil
from langchain.tools import tool
from security import check_path

@tool
def delete_item(path: str) -> str:
    """
    Delete a file or directory (recursively).

    Use this tool to remove a file or an entire directory permanently.
    All paths are relative to the 'output' directory or must be within it.

    Args:
        path: Relative or absolute path to the file/directory (must be inside 'output').

    Returns:
        "ok" if successfully deleted,
        or an error message starting with "Error: ".
    """
    try:
        safe_path = check_path(path)

        if not os.path.exists(safe_path):
            return "Error: No such file or directory"

        if os.path.isdir(safe_path):
            shutil.rmtree(safe_path)
        else:
            os.remove(safe_path)

        return "ok"

    except PermissionError as e:
        return f"Error: {e}"
    except OSError as e:
        return f"Error: {e}"