from peewee import Model, PostgresqlDatabase

from stilio.config import (
    DATABASE_NAME,
    DATABASE_HOST,
    DATABASE_PORT,
    DATABASE_USER,
    DATABASE_PASSWORD,
)

database = PostgresqlDatabase(
    DATABASE_NAME,
    host=DATABASE_HOST,
    port=DATABASE_PORT,
    user=DATABASE_USER,
    password=DATABASE_PASSWORD,
    autorollback=True,
)


class BaseModel(Model):
    class Meta:
        database = database


def init() -> None:
    from stilio.persistence.constants import MODELS

    with database.connection_context():
        database.create_tables(MODELS)
