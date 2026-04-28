import os

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from src.tools import tools
from .system_messages import system_messages

# Импорт агентов (предполагается, что они определены в текущем модуле или импортированы)
from .agents import (
    use_cases_agent,
    non_func_req_agent,
    func_req_agent,
    gen_app_plan_agent,
    code_gen_agent,
    tests_agent,
    tester_agent,
    docs_agent,
)
# ----------------------------------------------------------------------
# Инструменты запуска агентов
# ----------------------------------------------------------------------


@tool
def run_use_cases_agent(data: str) -> str:
    """
    Запускает агента «Юз-кейсы (Use Cases)».

    Args:
        data: Входной промпт для агента.

    Returns:
        Строка с результатом работы агента (например, сгенерированные use cases).
    """
    return use_cases_agent.run_agent(data)


@tool
def run_non_func_req_agent(data: str) -> str:
    """
    Запускает агента «Нефункциональные требования (НФТ)».

    Args:
        data: Входной промпт для агента.

    Returns:
        Строка с результатом работы агента.
    """
    return non_func_req_agent.run_agent(data)


@tool
def run_func_req_agent(data: str) -> str:
    """
    Запускает агента «Функциональные требования (ФТ)».

    Args:
        data: Входной промпт для агента.

    Returns:
        Строка с результатом работы агента.
    """
    return func_req_agent.run_agent(data)


@tool
def run_gen_app_plan_agent(data: str) -> str:
    """
    Запускает агента «Генерация плана кода».

    Args:
        data: Входной промпт для агента.

    Returns:
        Строка с результатом работы агента.
    """
    return gen_app_plan_agent.run_agent(data)


@tool
def run_code_gen_agent(data: str) -> str:
    """
    Запускает агента «Исходный код приложения».

    Args:
        data: Входной промпт для агента.

    Returns:
        Строка с результатом работы агента.
    """
    return code_gen_agent.run_agent(data)


@tool
def run_tests_agent(data: str) -> str:
    """
    Запускает агента «Тесты (unit / e2e)».

    Args:
        data: Входной промпт для агента.

    Returns:
        Строка с результатом работы агента.
    """
    return tests_agent.run_agent(data)


@tool
def run_tester_agent(data: str) -> str:
    """
    Запускает агента «Запуск тестов».

    Args:
        data: Входной промпт для агента.

    Returns:
        Строка с результатом работы агента.
    """
    return tester_agent.run_agent(data)


@tool
def run_docs_agent(data: str) -> str:
    """
    Запускает агента «Документация».

    Args:
        data: Входной промпт для агента.

    Returns:
        Строка с результатом работы агента.
    """
    return docs_agent.run_agent(data)



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
        
        self.tools = [
            *tools,
            run_use_cases_agent,
            run_non_func_req_agent,
            run_func_req_agent,
            run_gen_app_plan_agent,
            run_code_gen_agent,
            run_tests_agent,
            run_tester_agent,
            run_docs_agent
        ]

        
        self.agent = create_agent(
            model=self.llm,
            tools=self.tools
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
        
        print(answer)
        
        return answer

director_agent = Agent(
    system_message=str(system_messages.get("director")),
    name="Дирижёр",
    llm_name=os.getenv("DIRECTOR_MODEL", os.getenv("DEFAULT_MODEL"))
)