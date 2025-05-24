import requests
from google.adk.agents import Agent

GRAPHQL_ENDPOINT = "http://localhost:4000/"

def query_graphql(fields: list) -> dict:
    # Build the query string dynamically based on requested fields
    query_fields = "\n".join(fields)
    query = f"""
    query {{
        {query_fields}
    }}
    """
    payload = {"query": query}
    response = requests.post(GRAPHQL_ENDPOINT, json=payload)
    if response.status_code == 200:
        return {"status": "success", "data": response.json()}
    else:
        return {"status": "error", "error_message": response.text}

def find_data(user_input: str) -> dict:
    """Processes user input and queries the GraphQL API accordingly."""
    input_lower = user_input.lower()
    fields = []
    if "sales" in input_lower:
        fields.append("salesRecord")
    if "customer" in input_lower:
        fields.append("customer")
    if "product" in input_lower:
        fields.append("product")
    if not fields:
        # If no keywords found, return all fields
        fields = ["customer", "salesRecord", "product"]
    return query_graphql(fields)

root_agent = Agent(
    name="smart_data_finder",
    model="gemini-2.0-flash",
    description="Conversational agent to find sales records, customers, and products using a GraphQL API.",
    instruction=(
        "You are a helpful assistant. Engage in conversation, understand user requests about sales records, customers, or products, "
        "and fetch the relevant data from the GraphQL API."
    ),
    tools=[find_data],
)
