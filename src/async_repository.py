from sqlalchemy.ext.asyncio import AsyncEngine

from src.session_pool import SessionPool


class AsyncRepository:
    def __init__(self, engine: AsyncEngine):
        self.engine = engine

    async def insert_objects(self, batch):
        async with SessionPool(self.engine) as session:
            session.add_all(batch)
            await session.commit()
