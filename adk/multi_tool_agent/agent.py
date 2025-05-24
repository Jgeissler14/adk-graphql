import os
import requests
from google.adk.agents import Agent
import re

GRAPHQL_ENDPOINT = "http://localhost:4000/"

def log_to_file(message: str):
    with open("requests.log", "a") as f:
        f.write(message + "\n")


def query_graphql(query: str) -> dict:
    """Send a raw GraphQL query to the API and return the JSON response."""
    payload = {"query": query}
    response = requests.post(GRAPHQL_ENDPOINT, json=payload)
    if response.status_code == 200:
        return {"status": "success", "data": response.json()}
    else:
        return {"status": "error", "error_message": response.text}


def generate_graphql_query(user_input: str) -> str:
    """Generate a single-line GraphQL query from user input using Gemini, with no need for cleanup."""

    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError("GOOGLE_API_KEY environment variable not set")

    prompt = (
        "You are a GraphQL query generator. Respond ONLY with a valid GraphQL query, on a **single line**. "
        "Do not use newlines, backticks, markdown, or comments. Do not include any explanations. "
        "The output must start with 'query ExampleQuery {' and contain only valid top-level fields.\n\n"
        "Available fields: customer, salesRecord, product.\n\n"
        "Example:\n"
        "query ExampleQuery { customer salesRecord product }\n\n"
        "There are no nested fields, only top-level fields.\n\n"
        f"User request: {user_input}"
    )

    url = (
        "https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent"
        f"?key={api_key}"
    )

    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()

    candidate = response.json()["candidates"][0]
    raw_text = candidate["content"]["parts"][0]["text"].strip()

    log_to_file(f"Gemini response:\n{raw_text}")

    return raw_text

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
        "and fetch the relevant data from the GraphQL API. You should give it back to the user in the format they ask for (plain text, JSON, etc.),"
        "default to conversational responses as if you were their consultant."
    ),
    tools=[find_data],
)
