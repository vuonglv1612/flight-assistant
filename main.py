import uvicorn
from click import command, group

import config


@group()
def cli():
    pass


@command()
def api():
    uvicorn.run(
        "flight_assistant.api.app:app", host=config.API_HOST, port=config.API_PORT
    )


cli.add_command(api)

if __name__ == "__main__":
    cli()
