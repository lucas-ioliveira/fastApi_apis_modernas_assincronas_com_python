from typing import Generator

from sqlalchemy.ext.asyncio import AsyncSession
from secao04.core.database import Session


# from core.database import Session

# Fechando a conexãO após o uso.
async def get_session() -> Generator:
    session: AsyncSession = Session()

    try:
        yield session
    finally:
        await session.close()
