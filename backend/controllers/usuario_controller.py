from fastapi.requests import Request
from fastapi import UploadFile

from aiofile import async_open

from uuid import uuid4

from core.configs import settings
from core.database import get_session
from models.usuario_model import UsuarioModel
from controllers.base_controller import BaseController


class UsuarioController(BaseController):

    def __init__(self, request: Request) -> None:
        super().__init__(request, UsuarioModel)

    async def post_crud(self) -> None:
        form = await self.request.form()

        nome: str = form.get('nome')
        username: str = form.get('username')
        email: str = form.get('email')

        usuario: UsuarioModel = UsuarioModel(nome=nome, username=username, email=email)
    
        async with get_session() as session:
            
            session.add(usuario)
            await session.commit()

    async def put_crud(self, obj: object) -> None:
        async with get_session() as session:
            usuario: UsuarioModel = await session.get(self.model, obj.id)

            if usuario:
                form = await self.request.form()

                nome: str = form.get('nome')
                username: str = form.get('username')
                email: str = form.get('email')

                if nome and nome != usuario.nome:
                    usuario.nome = nome

                if username and username != usuario.username:
                    usuario.username = username

                if email and email != usuario.email:
                    usuario.email = email

                session.add(usuario)
                await session.commit()