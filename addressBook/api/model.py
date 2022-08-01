from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, ValidationError, validator


class UpdateAddressCordinates(BaseModel):
    longitude: int
    lattitude: int
    new_longitude: int
    new_lattitude: int

    ## Validating the address coordinates

    @validator('longitude')
    def validate_longitude(cls, longitude):
        if type(longitude) != int:
            raise ValidationError('must be integer')
        return longitude

    @validator('lattitude')
    def validate_lattitude(cls, lattitude):
        if type(lattitude) != int:
            raise ValueError('must be integer')
        return lattitude

    @validator('new_longitude')
    def validate_new_longitude(cls, new_longitude):
        if type(new_longitude) != int:
            raise ValidationError('must be integer')
        return new_longitude

    @validator('new_lattitude')
    def validate_new_lattitude(cls, new_lattitude):
        if type(new_lattitude) != int:
            raise ValueError('must be integer')
        return new_lattitude


class AddressCordinates(BaseModel):
    longitude: int
    lattitude: int

    ## Validating the address coordinates

    @validator('longitude')
    def validate_longitude(cls, longitude):
        if type(longitude) != int:
            raise ValueError('must be integer')
        return longitude

    @validator('lattitude')
    def validate_lattitude(cls, lattitude):
        if type(lattitude) != int:
            raise ValueError('must be integer')
        return lattitude
