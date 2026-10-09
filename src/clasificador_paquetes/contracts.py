from typing import Literal
from pydantic import BaseModel, ConfigDict, Field, field_validator


class Entrada(BaseModel):
    # TODO
    id_paquete: str = Field(min_length=1)

    peso_kg: float = Field(ge=0, le=30)

    distancia_km: float = Field()

    @field_validator(mode="after")
    @classmethod
    def delete_spaces(cls, id_paquete):
        try:
            id_paquete=id_paquete.strip()
        except ValueError as e:
            print(f"Error {e} al tratar la fila id_paquete")
        return id_paquete

    


class Salida(BaseModel):
    # TODO
    id_paquete: str = Field(min_length=1)

    categoria: Literal["normal", "urgente"]

    confianza: float = Field(ge=0, le=1)
