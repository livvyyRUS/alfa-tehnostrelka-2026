from .agent import Agent
from .system_messages import system_messages

use_cases_agent = Agent(
    system_message=str(system_messages.get("use_cases")), 
    name="Юз-кейсы (Use Cases)"
)

non_func_req_agent = Agent(
    system_message=str(system_messages.get("non_func_req")), 
    name="Нефункциональные требования (НФТ)"
)

func_req_agent = Agent(
    system_message=str(system_messages.get("func_req")), 
    name="Функциональные требования (ФТ)"
)

gen_app_plan_agent = Agent(
    system_message=str(system_messages.get("gen_app_plan")), 
    name="Генерация плана кода"
)

code_gen_agent = Agent(
    system_message=str(system_messages.get("code_gen")), 
    name="Исходный код приложения"
)

tests_agent = Agent(
    system_message=str(system_messages.get("tests")), 
    name="Тесты (unit / e2e)"
)

docs_agent = Agent(
    system_message=str(system_messages.get("docs")), 
    name="Документация"
)