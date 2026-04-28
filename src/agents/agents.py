import os

from .agent import Agent
from .system_messages import system_messages

use_cases_agent = Agent(
    system_message=str(system_messages.get("use_cases")), 
    name="Юз-кейсы (Use Cases)",
    llm_name=os.getenv("USE_CASES_MODEL", os.getenv("DEFAULT_MODEL"))
)

non_func_req_agent = Agent(
    system_message=str(system_messages.get("non_func_req")), 
    name="Нефункциональные требования (НФТ)",
    llm_name=os.getenv("NON_FUNC_REQ_MODEL", os.getenv("DEFAULT_MODEL"))
)

func_req_agent = Agent(
    system_message=str(system_messages.get("func_req")), 
    name="Функциональные требования (ФТ)",
    llm_name=os.getenv("FUNC_REQ_MODEL", os.getenv("DEFAULT_MODEL"))
)

gen_app_plan_agent = Agent(
    system_message=str(system_messages.get("gen_app_plan")), 
    name="Генерация плана кода",
    llm_name=os.getenv("GEN_APP_PLAN_MODEL", os.getenv("DEFAULT_MODEL"))
)

code_gen_agent = Agent(
    system_message=str(system_messages.get("code_gen")), 
    name="Исходный код приложения",
    llm_name=os.getenv("CODE_GEN_MODEL", os.getenv("DEFAULT_MODEL"))
)

tests_agent = Agent(
    system_message=str(system_messages.get("tests")), 
    name="Тесты (unit / e2e)",
    llm_name=os.getenv("TESTS_MODEL", os.getenv("DEFAULT_MODEL"))
)

tester_agent = Agent(
    system_message=str(system_messages.get("tester")),
    name="Запуск тестов",
    llm_name=os.getenv("TESTER_MODEL", os.getenv("DEFAULT_MODEL"))
)

docs_agent = Agent(
    system_message=str(system_messages.get("docs")), 
    name="Документация",
    llm_name=os.getenv("DOCS_MODEL", os.getenv("DEFAULT_MODEL"))
)