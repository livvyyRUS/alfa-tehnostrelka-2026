from pathlib import Path
from langchain.tools import tool
from .security import check_path

@tool
def makedir(path: str) -> str:
    """
    Create a new directory.

    Use this tool when you need to create a folder before writing files.
    All paths are relative to the 'output' directory or must be within it.

    Args:
        path: Relative or absolute path of the directory to create (must be inside 'output').

    Returns:
        "ok" if the directory was successfully created,
        "already exists" if it already exists,
        or an error message starting with "Error: ".
    """
    try:
        safe_path_str = check_path(path)
        _path = Path(safe_path_str)

        if _path.exists():
            if _path.is_dir():
                return "already exists"
            else:
                return f"Error: '{path}' exists but is not a directory"

        _path.mkdir(parents=True, exist_ok=True)
        return "ok"

    except PermissionError as e:
        return f"Error: {e}"
    except OSError as e:
        return f"Error: {e}"