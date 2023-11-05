"""Intragation tests for the API."""
from fastapi.testclient import TestClient
from pydantic_core._pydantic_core import ValidationError

from app.main import app
from app.models import TicketPagination, TicketWithMessagePagination

client = TestClient(app)


def test_read_main():
    """Test the health check endpoint."""
    response = client.get("/healthz")
    assert response.status_code == 200


def test_rate_limiter():
    """Test the rate limiter."""
    # Assuming you have a route that has a rate limit applied, you will call this endpoint
    # multiple times to trigger rate limiting
    response = None
    for _ in range(11):
        response = client.get("/healthz")

    # After exceeding the limit, you should get a 429 status code
    assert response.status_code == 429


def test_get_tickets():
    """Test the get_tickets endpoint."""
    # Override the dependencies if needed

    # Make the request to the endpoint
    response = client.get("/tickets?page=1&limit=10")

    # Check if the response is valid
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

    # Here we will need to manually match the response against the TicketPagination model
    # since the TestClient does not do response model validation
    try:
        TicketPagination(**response.json())
    except ValidationError as e:
        assert False, f"Response does not match the TicketPagination model: {e}"


def test_requests_not_found():
    """Test the get_tickets endpoint for a page that does not exist."""
    # Override the dependencies if needed

    # Make the request to the endpoint
    response = client.get("/tickets?page=100&limit=50")
    # Check if the response is valid
    assert response.status_code == 404

    response = client.get("/opentickets?page=100&limit=50")

    assert response.status_code == 404


def test_get_tickets_with_message():
    """Test the get_open_tickets endpoint."""
    # Override the dependencies if needed

    # Make the request to the endpoint
    response = client.get("/opentickets?page=1&limit=10")

    # Check if the response is valid
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

    # Here we will need to manually match the response against the TicketPagination model
    # since the TestClient does not do response model validation
    try:
        TicketWithMessagePagination(**response.json())
    except ValidationError as e:
        assert False, f"Response does not match the TicketPagination model: {e}"
