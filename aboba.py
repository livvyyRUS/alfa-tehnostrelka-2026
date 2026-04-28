from pathlib import Path

ALLOWED_EXTENSIONS = {".py", ".html", ".txt", ".qss"}
ALLOWED_FILENAMES = {".gitignore"}
EXCLUDED_DIRS = {".git", ".venv"}

SELF_NAME = "aboba.py"
OUTPUT_FILE = "aggregated_files.txt"

# Часть пути, которую нужно всегда вырезать
STRIP_PREFIX = "/home/roman/PycharmProjects"


def is_excluded(path: Path) -> bool:
    return any(part in EXCLUDED_DIRS for part in path.parts)


def should_take(path: Path) -> bool:
    if path.name == SELF_NAME:
        return False
    if path.name in ALLOWED_FILENAMES:
        return True
    return path.suffix.lower() in ALLOWED_EXTENSIONS


def collect_files(root: Path):
    files = []
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        if is_excluded(p):
            continue
        if should_take(p):
            files.append(p)
    files.sort(key=lambda p: p.as_posix())
    return files


def read_file(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return f"<Ошибка чтения файла: {e}>"


def strip_prefix(path: Path) -> str:
    full = path.resolve().as_posix()
    if full.startswith(STRIP_PREFIX):
        return full[len(STRIP_PREFIX):].lstrip("/")
    return full


def main():
    project_root = Path(__file__).parent.resolve()
    output_path = project_root / OUTPUT_FILE

    files = collect_files(project_root)
    files = [f for f in files if f.resolve() != output_path.resolve()]

    with output_path.open("w", encoding="utf-8", newline="\n") as out:
        for f in files:
            path_str = strip_prefix(f)
            content = read_file(f)

            out.write(f"{path_str}\n")
            out.write("{\n")
            out.write(content)
            out.write("\n}\n\n\n")   # 3 перевода строки

    print(f"Готово. Записано файлов: {len(files)}")
    print(f"Результат: {output_path}")


if __name__ == "__main__":
    main()
