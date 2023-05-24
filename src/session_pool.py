import asyncio

from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine


class SessionPool:
    pool_size = 0
    event = asyncio.Event()

    def __init__(self, engine: AsyncEngine):
        self.engine = engine

    async def __aenter__(self) -> AsyncSession:
        while True:
            if SessionPool.pool_size < 5:
                break
            await SessionPool.event.wait()
            SessionPool.event.clear()

        SessionPool.pool_size += 1
        return AsyncSession(self.engine)

    async def __aexit__(self, exc_type, exc, tb):
        SessionPool.pool_size -= 1

        if SessionPool.pool_size < 5:
            SessionPool.event.set()
