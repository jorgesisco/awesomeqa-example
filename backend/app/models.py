from datetime import datetime
from typing import List, Dict, Any, Optional
from pydantic import BaseModel


class Ticket(BaseModel):
    id: str
    msg_id: str
    status: str
    resolved_by: Optional[str] = None
    ts_last_status_change: Optional[str] = None
    timestamp: datetime
    context_messages: List[str]


class Pagination(BaseModel):
    total: int
    page: int
    limit: int
    data: List[Ticket]

# TODO: Create Message model to handle individual message data for tickets
