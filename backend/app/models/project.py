from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from .tables import specialist_project


class Project(Base):
    """Representa un Proyecto en la base de datos.
    Attributes:
        id (int): ID del proyecto.
        no_gespro (str):
        name (str): Nombre del proyecto.
        is_closed (bool): Indicador de que el proyecto ha finalizado.
        specialists (:obj:`list` of :obj:`Specialist`): Lista de especialistas asociados al proyecto
        hitos (:obj:`list` of :obj:`Hito`): Lista de hitos asociados al proyectos.
    """
    id = Column(Integer, primary_key=True, index=True)
    no_gespro = Column(String, index=True)
    name = Column(String)
    is_closed = Column(Boolean, default=False)
    specialists = relationship(
        'Specialist',
        secondary=specialist_project,
        back_populates='projects')
    hitos = relationship(
        'Hito',
        cascade='all, delate-orphan',
        backref='project'
    )


class Hito(Base):
    """Representa un Hito en la base de datos.
    Attributes:
        id (int): ID del Hito.
        number (int): Numero del Hito en el proyecto.
        hours (int): Cantidad de horas consumidas por el Hito.
        project_id (int): ID del proyecto asociado.
    """
    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer)
    hours = Column(Integer, default=0)
    project_id = Column(Integer, ForeignKey('project.id'))
