import subprocess
import shlex
import os
from langchain.tools import tool
from security import check_path, ALLOWED_BASE

def _is_path_arg(arg: str) -> bool:
    """
    Эвристика для определения, является ли аргумент командной строки файловым путём.
    """
    if not arg:
        return False
    # Абсолютный или относительный путь с указанием каталога
    if os.path.isabs(arg) or arg.startswith((".", "..")) or os.sep in arg:
        # Не считаем путём опции, начинающиеся с дефиса (например, -I/usr/include)
        if arg.startswith("-"):
            return False
        return True
    return False

@tool
def run_command(command: str) -> str:
    """
    Execute a system command inside the 'output' directory.

    Use this tool to run commands that process files.
    All file paths in the command must be inside the 'output' directory.
    The command runs with 'output' as the working directory without shell expansion.

    Args:
        command: The command with arguments (e.g. 'ls -la', 'python script.py').

    Returns:
        The combined stdout and stderr from the command,
        or an error message starting with "Error: ".
    """
    try:
        # Разбираем команду на части
        parts = shlex.split(command)
        if not parts:
            return "Error: empty command"

        safe_parts = []
        for part in parts:
            if _is_path_arg(part):
                # Если это потенциальный путь, проверяем и нормализуем
                safe = check_path(part)
                safe_parts.append(safe)
            else:
                safe_parts.append(part)

        # Выполняем команду без shell, с рабочим каталогом output
        result = subprocess.run(
            safe_parts,
            cwd=ALLOWED_BASE,
            capture_output=True,
            text=True,
            shell=False
        )

        output = result.stdout + result.stderr
        return output if output.strip() else "ok"

    except PermissionError as e:
        return f"Error: {e}"
    except FileNotFoundError:
        return f"Error: command not found: {parts[0] if 'parts' in locals() else command}"
    except OSError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Error: {e}"