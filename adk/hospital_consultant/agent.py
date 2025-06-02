"""Entry point for the hospital consultant multi-agent."""

from .agents.team_lead import team_lead_agent as agent, run_team_lead

__all__ = ["agent", "run_team_lead"]
