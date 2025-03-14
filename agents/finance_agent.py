from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools

def create_finance_agent():
    return Agent(
        name="finance-agent",
        model=Groq(id="deepseek-r1-distill-llama-70b"),
        tool=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
        instructions="Always include the source of the information you provide. Use tables to display data.",
        description="Get information about a company.",
        show_tool_calls=True,
        markdown=True,
        debug_mode=True,
    )