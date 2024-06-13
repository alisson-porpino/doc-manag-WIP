from sqlalchemy import String, Column, Boolean, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from core.configs import settings

class UsuarioModel(settings.DBBaseModel):
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(100))
	username: str = Column(String(40), unique=True, nullable=False)
	email: str = Column(String(120), unique=True, nullable=False)
	password: str = Column(String(255), nullable=False)
	#date_created: str = Column(DateTime(6), default=db.func.current_timestamp(), nullable=False)
	#last_update: str = Column(DateTime(6), onupdate=db.func.current_timestamp(), nullable=True)
	recovery_code: str = Column(String(200), nullable=True)
	department: str = Column(String(40), ForeignKey(Department.id), nullable=False)
	active: bool = Column(Boolean(), default=1, nullable=True)
	cargo: str = Column(Integer, ForeignKey(Cargo.id), nullable=False)

	#funcao = relationship(Cargo)
	#setor = relationship(Department)