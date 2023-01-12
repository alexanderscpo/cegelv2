from sqlalchemy import Table, ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

specialist_project = Table(
    "specialist_project",
    Base.metadata,
    Column("specialist_id", ForeignKey("specialist.id"), primary_key=True),
    Column('project_id', ForeignKey('project.id'), primary_key=True),
    category_id=Column(Integer, ForeignKey('category.id')),
    category=relationship('Category'),
    rol_id=Column(Integer, ForeignKey('rol.id')),
    rol=relationship('Rol'),
    year=Column('year', Integer),
    month=Column('month', String),
    hours=Column('hours', Integer, default=0)
)
