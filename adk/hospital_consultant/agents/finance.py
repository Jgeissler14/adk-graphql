from google.adk.agents import Agent
from ..utils import query_graphql

finance_agent = Agent(
    name="finance_agent",
    model="gemini-2.0-flash",
    description="Gives financial analysis and statistics.",
    instruction="Use hospital finance data to answer user questions via GraphQL.",
    tools=[query_graphql],
)
