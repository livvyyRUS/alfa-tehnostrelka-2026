from src.agents.director import director_agent
from pathlib import Path

path = Path("output")
if not path.exists():
    path.mkdir()

path = Path("input")
if not path.exists():
    path.mkdir()

director_agent.run_agent()
