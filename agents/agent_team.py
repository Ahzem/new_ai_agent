from phi.agent import Agent
from phi.model.groq import Groq
from .web_search_agent import create_web_search_agent
from .finance_agent import create_finance_agent

def create_agent_team():
    web_search_agent = create_web_search_agent()
    finance_agent = create_finance_agent()
    
    return Agent(
        team=[web_search_agent, finance_agent],
        model=Groq(id="deepseek-r1-distill-llama-70b"),
        instructions="Always include the source of the information you provide. Use tables to display data.",
        description="Get information about a company.",
        show_tool_calls=True,
        markdown=True,
        debug_mode=True,
    )