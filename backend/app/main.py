from app.repositories.ticket_repository import TicketRepository
import uvicorn
from fastapi import Depends, FastAPI
from fastapi.responses import JSONResponse
from pathlib import Path

app = FastAPI()

TICKET_FILEPATH = (Path(__file__).resolve().parent / "../data/awesome_tickets.json").resolve()
ticket_repository = TicketRepository(filepath=str(TICKET_FILEPATH))


@app.get("/healthz")
async def root():
    return "OK"


@app.get("/tickets")
async def get_tickets(
    limit: int = 20,
    ticket_repository: TicketRepository = Depends(lambda: ticket_repository),
):
    tickets = ticket_repository.get_tickets(limit)
    return JSONResponse(tickets, status_code=200)


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=5001, reload=True)
