from pathlib import Path
from langchain.tools import tool


@tool
def makedir(path: str) -> str:
    """
    Create a new directory.

    Use this tool when you need to create a folder before writing files.

    Args:
        path: Path of the directory to create.

    Returns:
        "ok" if the directory was successfully created.
    """
    _path = Path(path)
    if _path.exists():
        return "already exists"
    _path.mkdir()
    return "ok"
