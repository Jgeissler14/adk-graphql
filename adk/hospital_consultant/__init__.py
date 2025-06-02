"""Hospital consultant multi-agent package."""
from .agents.team_lead import run_team_lead
from .context import context_store

__all__ = ["run_team_lead", "context_store"]
