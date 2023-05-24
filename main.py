import asyncio
import os
from datetime import datetime

from sqlalchemy.engine import URL, create_engine
from sqlalchemy.ext.asyncio import create_async_engine

from src.async_repository import AsyncRepository
from src.document import Documento, Base
from src.repository import Repository

MAX_TIMEOUT_VALUE = 864000


def build_insert_list():
    insert_batch_list = []
    for i in range(100):
        insert_batch_list.append([
            Documento(id=None, identificador=j, conteudo=bytearray(os.urandom(100000))) for j in range(1000)
        ])

    return insert_batch_list


def regular_main(engine):
    repo = Repository(engine)
    for batch in build_insert_list():
        repo.insert_objects(batch)


async def async_main(engine):
    repo = AsyncRepository(engine)
    results = await asyncio.gather(
        *(
            repo.insert_objects(batch) for batch in build_insert_list()
        )
    )


def main():
    async_url = URL.create(
        "postgresql+asyncpg",
        username="postgres",
        password="postgres",
        host="127.0.0.1",
        port="6432",
        database="test_async"
    )
    async_engine = create_async_engine(async_url, pool_size=5, max_overflow=0, pool_pre_ping=True,
                                       pool_recycle=MAX_TIMEOUT_VALUE)

    regular_url = URL.create(
        "postgresql+psycopg2",
        username="postgres",
        password="postgres",
        host="127.0.0.1",
        port="6432",
        database="test_async"
    )
    engine = create_engine(regular_url)

    Base.metadata.create_all(engine)

    start_time = datetime.now()
    asyncio.run(async_main(async_engine))
    print("Async time: ", datetime.now() - start_time)

    start_time = datetime.now()
    regular_main(engine)
    print("Regular time: ", datetime.now() - start_time)


if __name__ == "__main__":
    main()
