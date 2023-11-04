"""Routes module."""
from app.config import ticket_repository
from app.models import Ticket, Pagination
from app.repositories.ticket_repository import TicketRepository
from fastapi import APIRouter, Depends, HTTPException, Query


router = APIRouter()


@router.get("/healthz")
async def root():
    """Health check endpoint."""
    return {"status": "OK"}


@router.get("/tickets")
async def get_tickets(
        page: int = Query(1, gt=0, description="Page number starting from 1"),
        limit: int = Query(20, gt=0, description="Number of tickets per page"),
        ticket_repository: TicketRepository = Depends(lambda: ticket_repository),
):
    """Get tickets with pagination."""
    offset = (page - 1) * limit
    total_tickets = ticket_repository.count_items(field="tickets")

    tickets_data = ticket_repository.get_tickets_with_messages(limit=limit, offset=offset)
    tickets = [Ticket(**ticket) for ticket in tickets_data]

    # Check if the current page is out of range
    if not tickets and page != 1:
        raise HTTPException(status_code=404, detail="Page not found")

    return Pagination(
        total=total_tickets,
        page=page,
        limit=limit,
        data=tickets
    )
