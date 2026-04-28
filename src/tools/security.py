import os

# Базовая директория, за пределы которой инструментам выходить запрещено
ALLOWED_BASE = os.path.realpath("output")

def check_path(path: str) -> str:
    """
    Проверяет, что переданный путь находится внутри ALLOWED_BASE.
    Возвращает абсолютный реальный путь, если доступ разрешён.
    В противном случае выбрасывает PermissionError с описанием.
    """
    if os.path.isabs(path):
        resolved = os.path.realpath(path)
    else:
        resolved = os.path.realpath(os.path.join(ALLOWED_BASE, path))

    if not (resolved == ALLOWED_BASE or resolved.startswith(ALLOWED_BASE + os.sep)):
        raise PermissionError(
            f"Access denied: '{path}' is outside the allowed directory '{ALLOWED_BASE}'"
        )
    return resolved