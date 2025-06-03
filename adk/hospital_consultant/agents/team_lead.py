"""Team lead agent coordinating hospital consultant specialists."""

from .billing import billing_agent
from .medical_report import medical_report_agent
from .pricing import pricing_agent
from .finance import finance_agent
from ..context import context_store


def _structured(agent_name: str, result: str) -> dict:
    """Return a basic structured payload for users."""
    return {"agent": agent_name, "result": result}


def run_team_lead(company_id: str, user_id: str, user_input: str) -> dict:
    """Delegate to a specialist agent and return a structured result."""
    # Import here to avoid circular dependency during initialization
    from ..agent import root_agent

    team_lead = root_agent
    lower = user_input.lower()
    context_store.add_user_message(company_id, user_id, f"user: {user_input}")

    if any(word in lower for word in ["bill", "invoice", "claim"]):
        result = billing_agent(user_input)
        context_store.add_user_message(company_id, user_id, f"billing_agent: {result}")
        return _structured("billing_agent", result)
    if any(word in lower for word in ["report", "record"]):
        result = medical_report_agent(user_input)
        context_store.add_user_message(company_id, user_id, f"medical_report_agent: {result}")
        return _structured("medical_report_agent", result)
    if "price" in lower or "cost" in lower:
        result = pricing_agent(user_input)
        context_store.add_user_message(company_id, user_id, f"pricing_agent: {result}")
        return _structured("pricing_agent", result)
    if "finance" in lower or "budget" in lower:
        result = finance_agent(user_input)
        context_store.add_user_message(company_id, user_id, f"finance_agent: {result}")
        return _structured("finance_agent", result)

    result = team_lead(user_input)
    context_store.add_user_message(company_id, user_id, f"team_lead: {result}")
    return _structured("team_lead", result)
