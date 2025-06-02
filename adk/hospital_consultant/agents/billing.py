from google.adk.agents import Agent
from ..utils import query_graphql

billing_agent = Agent(
    name="billing_agent",
    model="gemini-2.0-flash",
    description="Handles billing inquiries and insurance claims.",
    instruction="You respond to billing and insurance related questions using the hospital data graph.",
    tools=[query_graphql],
)
