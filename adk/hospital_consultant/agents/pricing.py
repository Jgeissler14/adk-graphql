from google.adk.agents import Agent
from ..utils import query_graphql

pricing_agent = Agent(
    name="pricing_agent",
    model="gemini-2.0-flash",
    description="Provides information on pricing and cost estimates.",
    instruction="Provide pricing information by querying the GraphQL API.",
    tools=[query_graphql],
)
