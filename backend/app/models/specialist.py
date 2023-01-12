from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from .tables import specialist_project


class Category(Base):
    """Representa la Categoria que se le puede asignar al especialista en un proyecto.

    Attributes:
        name (str): Nombre de la Categoria.
        fee (double): Tarifa de esta Categoria en un proyecto.
    """
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    fee = Column(DECIMAL(5, 2))


class Rol(Base):
    """Representa el Rol que se le puede asignar al especialista en un proyecto.

    Attributes:
        name (str): Nombre del Rol.
        fee (double): Tarifa del Rol en un proyecto.
    """
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    fee = Column(DECIMAL(5, 2))


class Specialist(Base):
    """Representa un especialista en la base de datos.

    Attributes:
        id (int): ID del especialista.
        first_name (str): Nombre del especialista.
        last_name (str): Apellidos del especialista.
        username (str): Usuario UCI del especialista.
        projects (:obj:`list` of :obj:`Project`): Lista de proyectos con los que tiene relación.
    """
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String)

    projects = relationship(
        "Project",
        secondary=specialist_project,
        back_populates="specialists"
    )


