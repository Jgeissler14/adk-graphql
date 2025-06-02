from google.adk.agents import Agent
from adk.multi_tool_agent.agent import find_data

pricing_agent = Agent(
    name="pricing_agent",
    model="gemini-2.0-flash",
    description="Provides information on pricing and cost estimates.",
    instruction="Provide pricing information by querying the GraphQL API.",
    tools=[find_data],
)
