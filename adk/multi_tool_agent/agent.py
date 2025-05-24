import os
import requests
from google.adk.agents import Agent

GRAPHQL_ENDPOINT = "http://localhost:4000/"

def query_graphql(query: str) -> dict:
    """Send a raw GraphQL query to the API and return the JSON response."""
    payload = {"query": query}
    response = requests.post(GRAPHQL_ENDPOINT, json=payload)
    if response.status_code == 200:
        return {"status": "success", "data": response.json()}
    else:
        return {"status": "error", "error_message": response.text}


def generate_graphql_query(user_input: str) -> str:
    """Generate a GraphQL query for the given user request using Gemini.

    The model should return a query referencing fields from the ``Query`` type.
    Available fields are:
      - ``customer``
      - ``salesRecord``
      - ``product``

    Example expected output::

        query {
            customer
            salesRecord
        }
    """

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")

    prompt = (
        "You are a helpful assistant that generates GraphQL queries. "
        "Return only the query. The possible fields are: customer, salesRecord, product.\n"
        f"User request: {user_input}"
    )

    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:"
        "generateContent?key=" + api_key
    )
    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    candidate = response.json()["candidates"][0]
    return candidate["content"]["parts"][0]["text"].strip()

def find_data(user_input: str) -> dict:
    """Generate a GraphQL query from user input using an LLM and execute it."""
    query = generate_graphql_query(user_input)
    return query_graphql(query)

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
