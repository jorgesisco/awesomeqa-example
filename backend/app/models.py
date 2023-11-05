"""Models for the API"""
from datetime import datetime
from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field


class Health(BaseModel):
    """Health check response model"""
    status: str = Field(examples=["OK"])
    version: str = Field(examples=["0.1.0"])


class Author(BaseModel):
    """Author of a message"""
    id: str
    name: str
    nickname: str
    color: Optional[str] = None  # Assuming color can be optional
    discriminator: str
    avatar_url: str
    is_bot: bool
    timestamp_insert: datetime


class Message(BaseModel):
    """
    Message that will be attached to a ticket for the requester to see
    """
    id: str
    channel_id: str

    parent_channel_id: Optional[str] = (
        Field(default=None,
        alias='parent_channel_id'))  # None is used if it can be null

    community_server_id: str
    timestamp: datetime
    has_attachment: bool

    reference_msg_id: Optional[str] = (
        Field(default=None,
              alias='reference_msg_id'))  # None is used if it can be null

    timestamp_insert: datetime

    discussion_id: Optional[str] = (
        Field(default=None,
              alias='discussion_id'))  # None is used if it can be null

    author_id: str
    content: str
    msg_url: str
    author: Author


class Ticket(BaseModel):
    """
    Ticket that will be displayed to the requester
    """
    id: str
    msg_id: str
    status: str
    resolved_by: Optional[str] = None
    ts_last_status_change: Optional[str] = None
    timestamp: datetime
    context_messages: List[str]
    message: Optional[Dict[str, Any]] = Field(None)


class TicketWithMessage(Ticket):
    """Ticket with message that will be displayed to the requester"""
    message: Optional[Message]


class TicketPagination(BaseModel):
    """Pagination response model"""
    total: int = Field(examples=[200])
    page: int = Field(examples=[1])
    limit: int = Field(examples=[20])
    data: List[Ticket]


class TicketWithMessagePagination(TicketPagination):
    """Pagination response model"""
    data: List[TicketWithMessage]
