from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
print(openai.api_key)
web_search_agent = Agent(
    name= "Web Search Agent",
   # model= OpenAIChat(id="gpt-4o-mini"),
    role= "Search the Web for the information",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    model= OpenAIChat(id="gpt-4o-mini"),
    #model = Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(analyst_recommendations=True,stock_price=True,company_news=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

agent_team = Agent(
    name= "Coordination Agent",
   # model= OpenAIChat(id="gpt-4o-mini"),
    model = Groq(id="llama-3.3-70b-versatile"),
    team=[web_search_agent,finance_agent],
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True
)

agent_team.print_response("Summarize analyst recommendations and share the latest news for Ford Motors", stream=True)