"""Context store implementations used by the hospital consultant agents."""

from __future__ import annotations

import json
import os
from typing import Dict, List, Tuple


class InMemoryContextStore:
    """Simple in-memory context store for demonstration.

    Stores per-company shared context and per-user chat history. In a real
    application this would be persisted in a database or other storage.
    """

    def __init__(self) -> None:
        self.company_context: Dict[str, Dict] = {}
        self.user_history: Dict[Tuple[str, str], List[str]] = {}

    # Company context
    def set_company_context(self, company_id: str, context: dict) -> None:
        self.company_context[company_id] = context

    def get_company_context(self, company_id: str) -> dict:
        return self.company_context.get(company_id, {})

    # User chat history
    def add_user_message(self, company_id: str, user_id: str, message: str) -> None:
        self.user_history.setdefault((company_id, user_id), []).append(message)

    def get_user_history(self, company_id: str, user_id: str) -> List[str]:
        return self.user_history.get((company_id, user_id), [])


class JsonFileContextStore(InMemoryContextStore):
    """Context store that persists data to a JSON file."""

    def __init__(self, file_path: str = None) -> None:
        self.file_path = file_path or os.getenv("CONTEXT_STORE_PATH", "context_store.json")
        super().__init__()
        self._load()

    # Persistence helpers -------------------------------------------------
    def _load(self) -> None:
        if not os.path.exists(self.file_path):
            return
        try:
            with open(self.file_path, "r", encoding="utf-8") as fh:
                data = json.load(fh)
        except json.JSONDecodeError:
            data = {}
        self.company_context = data.get("company_context", {})
        raw_history = data.get("user_history", {})
        self.user_history = {
            tuple(key.split("::")): value for key, value in raw_history.items()
        }

    def _save(self) -> None:
        data = {
            "company_context": self.company_context,
            "user_history": {"::".join(k): v for k, v in self.user_history.items()},
        }
        with open(self.file_path, "w", encoding="utf-8") as fh:
            json.dump(data, fh)

    # Overrides -----------------------------------------------------------
    def set_company_context(self, company_id: str, context: Dict) -> None:  # type: ignore[override]
        super().set_company_context(company_id, context)
        self._save()

    def add_user_message(self, company_id: str, user_id: str, message: str) -> None:  # type: ignore[override]
        super().add_user_message(company_id, user_id, message)
        self._save()


# Singleton instance used by the agents
context_store = JsonFileContextStore()
