# import statements
from pathlib import Path

import pytest
from app.config import TICKET_FILEPATH, ticket_repository


def test_ticket_repository_initialization():
    """
    Test that the TicketRepository is initialized with the correct filepath.
    """
    
    expected_filepath = Path(__file__).resolve().parent / "../data/awesome_tickets.json"

    assert ticket_repository.data
    assert ticket_repository.data["tickets"]
    assert expected_filepath.exists()
