"""Team lead agent coordinating hospital consultant specialists."""
from google.adk.agents import Agent

from .billing import billing_agent
from .medical_report import medical_report_agent
from .pricing import pricing_agent
from .finance import finance_agent
team_lead_agent = Agent(
    name="hospital_team_lead",
    model="gemini-2.0-flash",
    description="Coordinator for hospital and insurance queries.",
    instruction=(
        "You are the team lead for a group of specialist agents. Assess the user's request "
        "and delegate to the appropriate agent. Use billing_agent for billing questions, "
        "medical_report_agent for medical reports, pricing_agent for pricing, and finance_agent for finance."
    ),
    tools=[
        billing_agent,
        medical_report_agent,
        pricing_agent,
        finance_agent,
    ],
)
