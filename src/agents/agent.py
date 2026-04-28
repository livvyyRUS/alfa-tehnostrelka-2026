import os

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from src.tools import tools


class Agent():
    def __init__(self, system_message: str, name: str, llm_name: str = "qwen/qwen3.6-flash"):
        self.system_message = system_message
        self.name = name

        self.llm = ChatOpenAI(
            model=llm_name,   # или "gpt-3.5-turbo"
            temperature=0.8,
            api_key=os.getenv("API_KEY"), # API-ключ из переменной окружения
            base_url="https://openrouter.ai/api/v1"
        )


        self.agent = create_agent(
            model=self.llm,
            tools=tools
        )

    def run_agent(self, user_input: str = ""):
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
        answer = result["messages"][-1].content

        print(f'Шаг "{self.name}" успешно выполнен')

        return answer
