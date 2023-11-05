"""Pagination support for API routes.

This module provides utility functions for handling
pagination logic, including generating response parameters
and fetching paginated ticket data from the repository.
"""

from http.client import HTTPException
from app.models import TicketWithMessage, Ticket, TicketWithMessagePagination, TicketPagination
from app.repositories.ticket_repository import TicketRepository
from fastapi import HTTPException, Query


def response_params(
        page: int = Query(1, gt=0, description="Page number starting from 1"),
        limit: int = Query(20, gt=0, description="Number of tickets per page")
):
    return {
        "page": page,
        "limit": limit,
        "offset": (page - 1) * limit
    }


async def get_paginated_tickets(ticket_repository: TicketRepository, page: int, limit: int,
                                with_messages: bool = False):
    offset = (page - 1) * limit
    total_tickets = ticket_repository.count_items(field="tickets")

    if with_messages:
        tickets_data = ticket_repository.get_tickets_with_messages(limit=limit, offset=offset)
        ticket_model = TicketWithMessage
        pagination = TicketWithMessagePagination
    else:
        tickets_data = ticket_repository.get_tickets(limit=limit, offset=offset)
        ticket_model = Ticket
        pagination = TicketPagination

    tickets = [ticket_model(**ticket) for ticket in tickets_data]

    if not tickets and page != 1:
        raise HTTPException(status_code=404, detail="Page not found")

    return pagination(
        total=total_tickets,
        page=page,
        limit=limit,
        data=tickets
    )