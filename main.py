from src.agents import docs_agent, tests_agent, code_gen_agent, func_req_agent, use_cases_agent, non_func_req_agent, architecture_agent, file_manifest_agent, static_analysis_report_agent
from pathlib import Path

path = Path("output")
if not path.exists():
    path.mkdir()
    
path = Path("input")
if not path.exists():
    path.mkdir()

use_cases_agent.run_agent()
non_func_req_agent.run_agent()
func_req_agent.run_agent()
architecture_agent.run_agent()
file_manifest_agent.run_agent()
code_gen_agent.run_agent()
static_analysis_report_agent.run_agent()
tests_agent.run_agent()
docs_agent.run_agent()