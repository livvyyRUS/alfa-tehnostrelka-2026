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
        A comma-separated string of file and directory names.
    """
    return ",".join(os.listdir(path))