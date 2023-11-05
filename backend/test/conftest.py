import pytest
from datetime import datetime
from app.models import Author, Message, Ticket, TicketWithMessage


# Define a fixture for the current time that can be used in multiple tests
@pytest.fixture
def current_time():
    return datetime.now()


# Define a fixture for the author that can be used in multiple tests
@pytest.fixture
def test_author(current_time):
    return Author(
        id="123",
        name="John Doe",
        nickname="johnd",
        discriminator="0001",
        avatar_url="http://example.com/avatar.jpg",
        is_bot=False,
        timestamp_insert=current_time
    )


# Define a fixture for the message that can be used in multiple tests
@pytest.fixture
def test_message(current_time, test_author):
    return Message(
        id="msg1",
        channel_id="chan1",
        community_server_id="server1",
        timestamp=current_time,
        has_attachment=False,
        timestamp_insert=current_time,
        author_id="123",
        content="This is a test message",
        msg_url="http://example.com/message/1",
        author=test_author
    )


# Define a fixture for the ticket that can be used in multiple tests
@pytest.fixture
def test_ticket(current_time):
    return Ticket(
        id="ticket1",
        msg_id="msg1",
        status="open",
        timestamp=current_time,
        context_messages=["msg1", "msg2", "msg3"]
    )


@pytest.fixture
def test_ticket_with_message(test_ticket, test_message):
    """
    This fixture creates a TicketWithMessage instance using
    the test_ticket and test_message fixtures.
    """
    return TicketWithMessage(
        **test_ticket.model_dump(exclude={'message'}),  # Assuming you have a test_ticket fixture
        message=test_message  # Assuming you have a test_message fixture
    )
