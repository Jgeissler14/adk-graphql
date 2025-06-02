"""Hospital consultant multi-agent package."""
from .agent import agent
from .context import context_store
from .agents import run_team_lead
from .app import main as cli_main

__all__ = ["agent", "context_store", "run_team_lead", "cli_main"]
