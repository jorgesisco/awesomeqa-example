# Awesome ticket challenge

## Overview
This repository contains the code for the awesome ticket challenge.
Including both backend and frontend.

## Requirements
### Backend
- Python 3.8 or later
- FastAPI 0.104.1
- Uvicorn 0.23.2 as the ASGI server

### Frontend
- Node.js 16.x
- npm 10.x
- React 17.x
- @mui/material

## Getting Started
### Backend

Steps to setup the backend environment:

1. [Download the ticket data here](https://drive.google.com/file/d/1Bvk2mW5t3GfkqTkpURiFpaLuqrUckzUX/view?usp=sharing)
2. Place it in data/awesome_tickets.json
3. Run `make setup`
4. Run `make run`
5. Try it by calling [http://localhost:5001/tickets](http://localhost:5001/tickets)
6. API docs [http://localhost:5001/docs](http://localhost:5001/docs)

**Note:** you can also run the endpoints using the API documentation

#### Testing
Some unittests and integration tests are included in the backend. To run them type:

```bash
pytest
```

#### Testing coverage
If you want to check the testing coverage, run:

```bash
make coverage
```

### Frontend

1. Run `make setup`
2. Run `make run`
3. Open it: [http://localhost:3002](http://localhost:3002)

### Happy coding 🎉
