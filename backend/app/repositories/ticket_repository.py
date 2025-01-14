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

    def get_tickets_with_messages(self, limit: int, offset: int) -> list[dict]:
        """
        Return a slice of open tickets with their messages based
        on the offset and limit.
        """
        # Get tickets based on offset and limit
        tickets_data = self.get_tickets(limit=limit, offset=offset)

        # Create a new list containing only open tickets with message data
        open_tickets_with_messages = [
            self.append_message_to_ticket(ticket) for ticket in tickets_data if ticket.get('status') == 'open'
        ]

        return open_tickets_with_messages

    def append_message_to_ticket(self, ticket: dict) -> dict:
        """
        Appends message data to an open ticket, if a message ID is present.
        """
        msg_id = ticket.get('msg_id')
        # Ensure msg_id is present before attempting to fetch message
        if msg_id:
            # Retrieve the corresponding message
            message_data = self.get_message_by_id(msg_id)
            ticket['message'] = message_data if message_data else None
        else:
            # If there's no msg_id, set message to None
            ticket['message'] = None

        return ticket

    def get_message_by_id(self, msg_id: str) -> dict:
        """Return a message by its ID found in ticket."""
        # Retrieve the message by msg_id
        # This is a placeholder for however you retrieve messages
        message = next((msg for msg in self.data["messages"] if msg["id"] == msg_id), None)
        return message

    def count_items(self, field: str) -> int:
        """Return the total number of tickets or messages."""
        return len(self.data[field])

    def get_messages(self, limit: int, offset: int) -> list[dict]:
        """Return a slice of messages based on the offset and limit."""
        # If offset is beyond the number of messages, return an empty list
        if offset >= len(self.data["messages"]):
            return []

        # Calculate the maximum index to fetch
        end_index = offset + limit
        # Adjust if the end index is beyond the number of messages
        if end_index > len(self.data["messages"]):
            end_index = len(self.data["messages"])

        # Return the slice of messages
        return self.data["messages"][offset:end_index]
