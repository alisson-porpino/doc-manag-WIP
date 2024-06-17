from typing import Optional, List
from fastapi.requests import Request
from sqlalchemy.future import select

from core.database import get_session


class BaseController:

    def __init__(self, request: Request, model: object) -> None:
        self.request: Request = request
        self.model: object = model

    async def get_all_crud(self) -> Optional[List[object]]:
        async with get_session() as session:
            query = select(self.model)
            result = await session.execute(query)

            return result.scalars().all()
        
    async def get_one_crud(self, obj_id: int) -> Optional[object]:
        async with get_session() as session:
            obj: self.model = await session.get(self.model, obj_id)

            return obj
        
    async def post_crud(self) -> None:
        raise NotImplementedError("Não é um dado padrão. Faça a implementação em outras classes.")
    
    async def put_crud(self, obj: object) -> None:
        raise NotImplementedError("Não é um dado padrão. Faça a implementação em outras classes.")
    
    async def del_crud(self, obj_id: int) -> None:
        async with get_session() as session:
            obj: self.model = await session.get(self.model, obj_id)

            if obj:
                await session.delete(obj)
                await session.commit()