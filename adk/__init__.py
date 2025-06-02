"""Top-level ADK package with optional helper imports."""

# Lazy accessors to avoid heavy imports when the package is only used for CLI

def run_team_lead(*args, **kwargs):
    from .hospital_consultant import run_team_lead as _run
    return _run(*args, **kwargs)


def get_context_store():
    from .hospital_consultant import context_store
    return context_store

__all__ = ["run_team_lead", "get_context_store"]
