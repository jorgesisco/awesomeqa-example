"""Routes module."""
from app.config import ticket_repository
from app.models import TicketPagination, TicketWithMessagePagination, Health
from app.repositories.ticket_repository import TicketRepository
from fastapi import APIRouter, Depends

from app.utils.pagination import response_params, get_paginated_tickets

router = APIRouter()


@router.get("/healthz", response_model=Health)
async def root():
    """Health check endpoint."""
    return {
            "status": "OK",
            "version": "0.1.0"
            }


@router.get("/tickets", response_model=TicketPagination)
async def get_tickets(
        common: dict = Depends(response_params),
        ticket_repository: TicketRepository = Depends(lambda: ticket_repository)
):
    """Return a list of tickets from json file."""
    return await get_paginated_tickets(
        ticket_repository=ticket_repository,
        page=common['page'],
        limit=common['limit'],
        with_messages=False
    )


@router.get("/opentickets", response_model=TicketWithMessagePagination)
async def get_open_tickets(
        common: dict = Depends(response_params),
        ticket_repository: TicketRepository = Depends(lambda: ticket_repository)
):
    """
    Return a list of open tickets with their messages
    from json file
    """
    return await get_paginated_tickets(
        ticket_repository=ticket_repository,
        page=common['page'],
        limit=common['limit'],
        with_messages=True
    )
