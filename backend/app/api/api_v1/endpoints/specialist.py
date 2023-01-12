from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import dependencies

router = APIRouter()


@router.get('/', response_model=List[schemas.Specialist])
def read_specialists(
        *,
        db: Session = Depends(dependencies.get_db),
        skip: int = 0,
        limit: int = 10,
        current_user: models.User = Depends(dependencies.get_current_active_user)
) -> Any:
    """
    Obtener todos los especialista
    """
    pass


@router.get('/', response_model=schemas.Specialist)
def create_specialist(
        *,
        db: Session = Depends(dependencies.get_db),
        specialist_in: schemas.SpecialistCreate,
        current_user: models.User = Depends(dependencies.get_current_active_user)
) -> Any:
    """
    Crear un nuevo especialista.
    """
    specialist = crud.specialist.create_with_owner(db=db, obj_in=specialist_in)  # Arreglar
    return specialist


@router.put('/{specialist_id}', response_model=schemas.Specialist)
def update_specialist(
        *,
        db: Session = Depends(dependencies.get_db),
        specialist_id: int,
        specialist_in: schemas.SpecialistUpdate,
        current_user: models.User = Depends(dependencies.get_current_active_user)
) -> Any:
    """
    Actualizar un especialista dado el [id]
    """
    specialist = crud.specialist.get(db=db, id=specialist_id)
    if not specialist:
        raise HTTPException(status_code=404, detail='Especialista no encontrado')
    if not crud.user.is_superuser(current_user) and (specialist.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail='No tienes suficientes permisos para solicitar este recurso')
    specialist = crud.specialist.update(db=db, db_obj=specialist, obj_in=specialist_in)
    return specialist


@router.get('/{specialist_id}', response_model=schemas.Specialist)
def read_specialist(
        *,
        db: Session = Depends(dependencies.get_db),
        specialist_id: int,
        current_user: models.User = Depends(dependencies.get_current_active_user)
) -> Any:
    """
    Obtener un especialista dado el [id]
    """
    specialist = crud.specialist.get(db=db, id=specialist_id)
    if not specialist:
        raise HTTPException(status_code=404, detail='Especialista no encontrado')
    if not crud.user.is_superuser(current_user) and (specialist.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail='No tienes suficientes permisos para solicitar este recurso')
    return specialist


@router.delete('/{specialist_id}', response_model=schemas.Specialist)
def delete_specialist(
        *,
        db: Session = Depends(dependencies.get_db),
        specialist_id: int,
        current_user: models.User = Depends(dependencies.get_current_active_user)
) -> Any:
    """
    Eliminar un especialista dado el [id]
    """
    specialist = crud.specialist.get(db=db, id=specialist_id)
    if not specialist:
        raise HTTPException(status_code=404, detail='Especialista no encontrado')
    if not crud.user.is_superuser(current_user) and (specialist.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail='No tienes suficientes permisos para solicitar este recurso')
    specialist = crud.specialist.remove(db=db, id=specialist_id)
    return specialist
