from .agent import Agent
from .system_messages import system_messages

use_cases_agent = Agent(
    system_message=str(system_messages.get("use_cases"))
)

non_func_req_agent = Agent(
    system_message=str(system_messages.get("non_func_req"))
)

func_req_agent = Agent(
    system_message=str(system_messages.get("func_req"))
)

code_gen_agent = Agent(
    system_message=str(system_messages.get("code_gen"))
)

tests_agent = Agent(
    system_message=str(system_messages.get("tests"))
)

docs_agent = Agent(
    system_message=str(system_messages.get("docs"))
)