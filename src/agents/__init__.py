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

architecture_agent = Agent(
    system_message=str(system_messages.get("architecture")), 
    name="Архитектура и разбиение на модули"
)

file_manifest_agent = Agent(
    system_message=str(system_messages.get("file_manifest")), 
    name="Файловая структура"
)

code_gen_agent = Agent(
    system_message=str(system_messages.get("code_gen")), 
    name="Исходный код приложения"
)

static_analysis_report_agent = Agent(
    system_message=str(system_messages.get("static-analysis-report")), 
    name="Статический анализ и автоисправление"
)

tests_agent = Agent(
    system_message=str(system_messages.get("tests")), 
    name="Тесты (unit / e2e)"
)

docs_agent = Agent(
    system_message=str(system_messages.get("docs")), 
    name="Документация"
)