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


@command()
def migrate():
    from alembic import command
    from alembic.config import Config

    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")


@command()
def seeding():
    from seeding import seeding

    seeding.run("./seeding/rules.json")


cli.add_command(api)
cli.add_command(migrate)
cli.add_command(seeding)

if __name__ == "__main__":
    cli()
