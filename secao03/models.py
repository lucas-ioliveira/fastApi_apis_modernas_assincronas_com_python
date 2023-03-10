from typing import Optional
from pydantic import BaseModel, validator


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    @validator('titulo')
    def validar_titulo(cls, value: str):
        # Validação 1
        palavras = value.split(' ')
        if len(palavras) < 3:
            raise ValueError('O título deve ter pelo menos três palavras.')
        
        # Validação 2
        if value.islower():
            raise ValueError('O título deve ser capitalizado.')

        return value
    
    @validator('aulas')
    def validar_aulas(cls, value: int):
        # Validação 1
        if value < 12:
            raise ValueError('A quantidade de aulas tem que ser maior 12.')
        return value

    @validator('horas')
    # Validação 1
    def validar_horas(cls, value: int):
        if value < 10:
            raise ValueError('horas deve ser maior 10')
 
        return value

cursos = [
    Curso(id=1, titulo='Programação para Leigos', aulas=42, horas=56),
    Curso(id=2, titulo="Algoritmos e Lógica de programação", aulas=52, horas=66),
]
