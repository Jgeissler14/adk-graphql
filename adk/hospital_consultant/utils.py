import requests

GRAPHQL_ENDPOINT = "http://localhost:4000/"


def query_graphql(query: str) -> dict:
    """Send a GraphQL query to the mocked API and return the JSON response."""
    response = requests.post(GRAPHQL_ENDPOINT, json={"query": query})
    if response.status_code == 200:
        return {"status": "success", "data": response.json()}
    return {"status": "error", "error_message": response.text}
