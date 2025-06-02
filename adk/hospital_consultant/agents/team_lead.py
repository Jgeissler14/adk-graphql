"""Team lead agent coordinating hospital consultant specialists."""
from google.adk.agents import Agent

from .billing import billing_agent
from .medical_report import medical_report_agent
from .pricing import pricing_agent
from .finance import finance_agent


def _create_team_lead() -> Agent:
    """Factory for the team lead agent."""
    return Agent(
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


def run_team_lead(user_input: str):
    """Simple delegation logic based on keywords."""
    team_lead = _create_team_lead()
    lower = user_input.lower()
    if any(word in lower for word in ["bill", "invoice", "claim"]):
        return billing_agent(user_input)
    if any(word in lower for word in ["report", "record"]):
        return medical_report_agent(user_input)
    if "price" in lower or "cost" in lower:
        return pricing_agent(user_input)
    if "finance" in lower or "budget" in lower:
        return finance_agent(user_input)
    return team_lead(user_input)
