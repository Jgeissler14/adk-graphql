class InMemoryContextStore:
    """Simple in-memory context store for demonstration.

    Stores per-company shared context and per-user chat history. In a real
    application this would be persisted in a database or other storage.
    """

    def __init__(self):
        self.company_context = {}
        self.user_history = {}

    # Company context
    def set_company_context(self, company_id: str, context: dict) -> None:
        self.company_context[company_id] = context

    def get_company_context(self, company_id: str) -> dict:
        return self.company_context.get(company_id, {})

    # User chat history
    def add_user_message(self, company_id: str, user_id: str, message: str) -> None:
        self.user_history.setdefault((company_id, user_id), []).append(message)

    def get_user_history(self, company_id: str, user_id: str):
        return self.user_history.get((company_id, user_id), [])


# Singleton instance used by the agents
context_store = InMemoryContextStore()
