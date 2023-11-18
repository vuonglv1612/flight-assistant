# flight-assistant

A flight assistant using OpenAI API.

## Installation

### Install Dependencies

```bash
sudo apt install build-essential python3.10-venv python3.10-dev libpq-dev -y
```

### Install Python Dependencies

```bash
python3.10 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Configure Environment Variables

```bash
export API_HOST=localhost
export API_PORT=8000
export ENGINE_POSTGRES_URI=postgresql://flight:psql@localhost:5432/engine
export OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
export OPENAI_SUMMARIZE_MODEL=gpt-3.5-turbo-1106
export OPENAI_SUMMARIZE_TEMPERATURE=0.2
export OPENAI_SUMMARIZE_MAX_TOKENS=512
```

## Run

### Migration

```bash
./.venv/bin/python main.py migrate
```

### Seeding sample data

```bash
./.venv/bin/python main.py seeding
```

### Run API

```bash
./.venv/bin/python main.py api
```

## Usage
### List all Booking Product
```bash
curl -X GET http://localhost:8000/booking-products?page=1&page_size=5
```

### Generate Fare Rules Summary
```bash
curl -X POST http://localhost:8000/booking-products/<booking-product-id>/fare-rules-summary
```

### Detail Document
Web: http://localhost:8000/docs

