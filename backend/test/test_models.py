from datetime import datetime
from app.models import Health, Author, Message, Ticket, TicketWithMessage, TicketPagination, TicketWithMessagePagination


def test_health_model():
    """Test the Health model"""

    health = Health(status="OK", version="1.0.0")
    assert health.status == "OK"
    assert health.version == "1.0.0"


def test_author_model(test_author):
    """test_author is a fixture defined in backend/test/conftest.py"""

    assert test_author.id == "123"
    assert test_author.name == "John Doe"
    assert test_author.nickname == "johnd"
    assert test_author.discriminator == "0001"
    assert test_author.avatar_url == "http://example.com/avatar.jpg"
    assert test_author.is_bot is False
    assert test_author.timestamp_insert is not None


def test_message_model(test_message):
    assert test_message.id == "msg1"
    assert test_message.content == "This is a test message"
    assert test_message.author.nickname == "johnd"
    assert test_message.author.avatar_url == "http://example.com/avatar.jpg"
    assert test_message.author.is_bot is False
    assert test_message.timestamp_insert is not None


def test_ticket_model(test_ticket):
    """test_ticket is a fixture defined in backend/test/conftest.py"""

    assert test_ticket.id == "ticket1"
    assert test_ticket.msg_id == "msg1"
    assert test_ticket.status == "open"
    assert test_ticket.timestamp is not None
    assert test_ticket.context_messages == ["msg1", "msg2", "msg3"]
    assert test_ticket.message is None


def test_ticket_with_message_model(current_time, test_ticket, test_message):
    """test_ticket and test_message are fixtures defined in backend/test/conftest.py"""
    # Create a dictionary from the test_ticket excluding 'message'
    ticket_dict = test_ticket.model_dump(exclude={'message'})

    ticket_with_message = TicketWithMessage(
        **ticket_dict,
        message=test_message
    )
    assert ticket_with_message.id == test_ticket.id
    assert ticket_with_message.message.id == test_message.id
    assert ticket_with_message.message.content == test_message.content
    assert ticket_with_message.message.author.nickname == test_message.author.nickname
    assert ticket_with_message.message.author.avatar_url == test_message.author.avatar_url
    assert ticket_with_message.message.author.is_bot == test_message.author.is_bot
    assert ticket_with_message.message.timestamp_insert == test_message.timestamp_insert


def test_ticket_pagination_model(test_ticket):
    ticket_pagination = TicketPagination(
        total=100,
        page=2,
        limit=20,
        data=[test_ticket]
    )
    assert ticket_pagination.total == 100
    assert ticket_pagination.total == 100
    assert ticket_pagination.page == 2
    assert ticket_pagination.limit == 20
    assert len(ticket_pagination.data) == 1


def test_ticket_with_message_pagination_model(test_ticket_with_message):
    """test_ticket_with_message is a fixture defined in backend/test/conftest.py"""

    ticket_with_message_pagination = TicketWithMessagePagination(
        total=100,
        page=2,
        limit=20,
        data=[test_ticket_with_message]
    )
    assert ticket_with_message_pagination.total == 100
    assert len(ticket_with_message_pagination.data) == 1
    assert ticket_with_message_pagination.data[0].id == test_ticket_with_message.id

    # This line checks for the presence of a message, which should not be None
    assert ticket_with_message_pagination.data[0].message is not None

