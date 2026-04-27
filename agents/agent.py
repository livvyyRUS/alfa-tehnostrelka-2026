from langchain.agents import create_agent
from llm import llm
from tools import tools

class Agent():
    def __init__(self, system_message: str):
        self.system_message = system_message
        
        self.agent = create_agent(
            model=llm,
            tools=tools
        )

    def run_agent(self, user_input: str):
        result = self.agent.invoke({
            "messages": [
                {
                "role": "system",
                "content": self.system_message
                },
                {
                    "role": "user", 
                    "content": user_input
                }
            ]
        })

        return result["messages"][-1].content
