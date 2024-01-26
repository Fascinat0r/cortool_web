from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase):
    pass


role = Table(
    "role",
    Base.metadata,
    Column("role_id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    role_id = Column(Integer, ForeignKey(role.c.role_id))
    email: Mapped[str] = mapped_column(
        String(length=320), unique=True, index=True, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(
        String(length=1024), nullable=False
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )


# class ComponentAssociation(Base):
#     __tablename__ = 'component_association'
#     parent_id = mapped_column(Integer, ForeignKey('component.id'), primary_key=True)
#     child_id = mapped_column(Integer, ForeignKey('component.id'), primary_key=True)
#     postfix = mapped_column(String)
#
#
# class Component(Base):
#     __tablename__ = 'component'
#
#     id = mapped_column(Integer, primary_key=True)
#     name = mapped_column(String, nullable=False)
#     description = mapped_column(String)
#     creator_id = mapped_column(Integer)
#     date = mapped_column(TIMESTAMP)
#     data = mapped_column(JSON, nullable=False)
#     is_final = mapped_column(Boolean, nullable=False)
#
#     parents = relationship(
#         'Component',
#         secondary='component_association',
#         primaryjoin='Component.id==ComponentAssociation.child_id',
#         secondaryjoin='Component.id==ComponentAssociation.parent_id',
#         backref='children'
#     )
#
#
# class System(Base):
#     __tablename__ = 'system'
#     parent_id = mapped_column(Integer, ForeignKey('component.id'), primary_key=True)
#
#
# class Material(Base):
#     __tablename__ = 'material'
#
#     id = mapped_column(Integer, primary_key=True)
#     name = mapped_column(String)
#     manufacturer = mapped_column(String)
#     data = mapped_column(JSON, nullable=False)
#
#
# class MaterialAssociation(Base):
#     __tablename__ = 'material_association'
#
#     component_id = mapped_column(Integer, ForeignKey('component.id'), primary_key=True)
#     material_id = mapped_column(Integer, ForeignKey('material.id'), primary_key=True)
#
#     # Relationships
#     component = relationship('Component', backref='material_associations')
#     material = relationship('Material', backref='component_associations')
