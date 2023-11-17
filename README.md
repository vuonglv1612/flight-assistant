# flight-assistant

A flight assistant using OpenAI API.


## Installation
### Install Dependencies
```bash
sudo apt install build-essential python3.10-venv python3.10-dev libpg-dev -y
```

### Install Python Dependencies
```bash
python3.10 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```


### Configure Environment Variables
```bash
export OPENAI_TOKEN=xxxx
export ENGINE_DB_URI=postgresql://postgres:postgres@localhost:5432/postgres
```