from pathlib import Path

from app.repositories.ticket_repository import TicketRepository

TICKET_FILEPATH = Path(__file__).resolve().parent / "../data/awesome_tickets.json"
ticket_repository = TicketRepository(filepath=TICKET_FILEPATH)
