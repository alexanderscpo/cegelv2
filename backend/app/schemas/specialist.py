from typing import Optional

from pydantic import BaseModel


class SpecialistBase(BaseModel):
    pass


class SpecialistCreate(SpecialistBase):
    pass


class SpecialistUpdate(SpecialistBase):
    pass


class SpecialistInDBBase(SpecialistBase):
    pass


class Specialist(SpecialistInDBBase):
    pass


class SpecialistInDB(SpecialistInDBBase):
    pass