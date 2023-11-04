import json
from pathlib import Path
from typing import Optional


class TicketRepository:
    """
    A simple repository to fetch tickets and messages
    from a JSON file.
     """
    def __init__(self, filepath: str | Path):
        with open(filepath) as json_file:
            self.data = json.load(json_file)

    def get_tickets(self, offset: int, limit: Optional[int] = None) -> list[dict]:
        """
        Return a slice of tickets based on the offset and limit.
        or all tickets if limit is not specified.
        """
        # If the offset is greater than the number of tickets, return an empty list
        if offset >= len(self.data["tickets"]):
            return []

        # If limit is not specified, or is greater than the number of available tickets,
        # adjust it to return all remaining tickets
        if limit is None or offset + limit > len(self.data["tickets"]):
            limit = len(self.data["tickets"]) - offset

        # Return the slice of tickets based on the offset and limit
        return self.data["tickets"][offset:offset + limit]

    def count_tickets(self) -> int:
        """Return the total number of tickets."""
        return len(self.data["tickets"])

    def get_messages(self, limit: Optional[int] = None) -> list[dict]:
        """
        Return default limit set in route or total
        messages if limit is None.
        """
        if limit is None:
            return self.data["messages"]
        else:
            return self.data["messages"][:limit]


