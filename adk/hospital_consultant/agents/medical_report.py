from google.adk.agents import Agent
from ..utils import query_graphql

medical_report_agent = Agent(
    name="medical_report_agent",
    model="gemini-2.0-flash",
    description="Specialist in medical reports and patient records.",
    instruction="Answer questions about medical reports or records. Use the GraphQL API for data.",
    tools=[query_graphql],
)
