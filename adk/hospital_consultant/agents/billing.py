from google.adk.agents import Agent
from adk.multi_tool_agent.agent import find_data

billing_agent = Agent(
    name="billing_agent",
    model="gemini-2.0-flash",
    description="Handles billing inquiries and insurance claims.",
    instruction="You respond to billing and insurance related questions using the hospital data graph.",
    tools=[find_data],
)
