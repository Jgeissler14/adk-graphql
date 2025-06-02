"""Utility helpers used across the hospital consultant package."""

from __future__ import annotations

import logging
import os
from typing import Any, Dict

import requests


GRAPHQL_ENDPOINT = os.getenv("GRAPHQL_ENDPOINT", "http://localhost:4000/")

logger = logging.getLogger(__name__)


def query_graphql(query: str) -> Dict[str, Any]:
    """Send a GraphQL query to the API and return the JSON response."""
    try:
        response = requests.post(GRAPHQL_ENDPOINT, json={"query": query}, timeout=5)
        response.raise_for_status()
        return {"status": "success", "data": response.json()}
    except requests.RequestException as exc:  # pragma: no cover - network errors
        logger.exception("GraphQL query failed: %s", exc)
        return {"status": "error", "error_message": str(exc)}
