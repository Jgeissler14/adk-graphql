from google.adk.agents import Agent
from adk.multi_tool_agent.agent import find_data

finance_agent = Agent(
    name="finance_agent",
    model="gemini-2.0-flash",
    description="Gives financial analysis and statistics.",
    instruction="Use hospital finance data to answer user questions via GraphQL.",
    tools=[find_data],
)
