"""Team lead agent coordinating hospital consultant specialists."""
from __future__ import annotations

from typing import Any, Dict

from google.adk.agents import Agent

from ..context import context_store

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


def run_team_lead(company_id: str, user_id: str, message: str) -> Dict[str, Any]:
    """Run the team lead agent and capture conversation history."""
    context_store.add_user_message(company_id, user_id, f"user:{message}")

    # The ADK Agent implements ``__call__`` for interaction. If a different API
    # is required, update this call site accordingly.
    if hasattr(team_lead_agent, "chat"):
        result = team_lead_agent.chat(message)
    else:  # pragma: no cover - depends on ADK implementation
        result = team_lead_agent(message)

    context_store.add_user_message(company_id, user_id, f"agent:{result}")

    return {"_structured": {"response": result}}
