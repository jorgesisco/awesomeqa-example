from app.config import ticket_repository
from app.repositories.ticket_repository import TicketRepository
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/healthz")
async def root():
    """Health check endpoint."""
    return "OK"


@router.get("/tickets")
async def get_tickets(
        limit: int = 20,
        ticket_repository: TicketRepository = Depends(lambda: ticket_repository),
):
    """Get tickets endpoint."""
    tickets = ticket_repository.get_tickets(limit)
    return JSONResponse(tickets, status_code=200)

