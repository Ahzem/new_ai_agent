from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo

def create_web_search_agent():
    return Agent(
        name="web-search-agent",
        model=Groq(id="deepseek-r1-distill-llama-70b"),
        tool=[DuckDuckGo()],
        instructions="Always include the source of the information you provide. write short and concise",
        description="Search the web for information.",
        show_tool_calls=True,
        markdown=True,
        debug_mode=True,
    )