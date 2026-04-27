import os
from pathlib import Path

system_messages = {
    
}

for prompt_file in os.listdir("promts"):
    path = Path("promts", prompt_file)
    with open(path, "r", encoding="utf8") as file:
        prompt = file.read()
        system_messages[path.stem] = prompt