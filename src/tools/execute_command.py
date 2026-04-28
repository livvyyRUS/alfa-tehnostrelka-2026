import subprocess
from langchain.tools import tool


@tool
def execute_command(command: str) -> str:
    """
    Execute a shell command on the system.

    Use this tool when you need to run a terminal command.

    Args:
        command: The command to execute.

    Returns:
        The command output (stdout + stderr) or an error message
        starting with "Error: ".
    """
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )

        output = result.stdout.strip()
        error = result.stderr.strip()

        if result.returncode != 0:
            return f"Error: {error or 'Command failed with non-zero exit code'}"

        return output or "Command executed successfully (no output)"

    except Exception as e:
        return f"Error: {e}"