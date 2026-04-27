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
        "ok" if the file was successfully written.
    """
    with open(path, "w", encoding="utf-8") as file:
        file.write(data)
    return "ok"