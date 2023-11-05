"""Routes module."""
from app.config import ticket_repository
from app.utils.rate_limit import limiter
from app.models import TicketPagination, TicketWithMessagePagination, Health
from app.repositories.ticket_repository import TicketRepository
from fastapi import APIRouter, Request, Depends

from app.utils.pagination import response_params, get_paginated_tickets

router = APIRouter()


@router.get("/healthz", response_model=Health)
@limiter.limit("10/minute")
async def root(request: Request):
    """Health check endpoint."""
    return {
            "status": "OK",
            "version": "0.1.0"
            }


@router.get("/tickets", response_model=TicketPagination)
@limiter.limit("5/minute")
async def get_tickets(
        request: Request,
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
@limiter.limit("5/minute")
async def get_open_tickets(
        request: Request,
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
