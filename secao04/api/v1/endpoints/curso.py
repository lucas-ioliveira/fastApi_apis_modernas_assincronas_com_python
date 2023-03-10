from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from secao04.models.curso_model import CursoModel
from secao04.schemas.curso_schema import CursoSchema
from secao04.core.deps import get_session

# from models.curso_model import CursoModel
# from schemas.curso_schema import CursoSchema
# from core.deps import get_session

router = APIRouter()


# Post curso


@router.post('/', response_model=CursoSchema, status_code=status.HTTP_201_CREATED)
async def post_curso(curso: CursoSchema, db: AsyncSession = Depends(get_session)):
    novo_curso = CursoModel(titulo=curso.titulo,
                            aulas=curso.aulas, horas=curso.horas)
    db.add(novo_curso)
    await db.commit()

    return novo_curso


# Get cursos


@router.get('/', response_model=List[CursoSchema])
async def get_cursos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel)
        result = await session.execute(query)
        cursos: List[CursoModel] = result.scalars().all()

        return cursos


# Get curso


@router.get('/ {curso_id}', response_model=CursoSchema, status_code=status.HTTP_200_OK)
async def get_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db as sesssion:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await sesssion.execute(query)
        curso = result.scalar_one_or_none()

        if curso:
            return curso
        else:
            raise HTTPException(detail='Curso não encontrado.',
                                status_code=status.HTTP_404_NOT_FOUND)


# Put curso


@router.put('/{curso_id}', response_model=CursoSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_curso(curso_id: int, curso: CursoSchema, db: AsyncSession = Depends(get_session)):
    async with db as sesssion:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await sesssion.execute(query)
        curso_up = result.scalar_one_or_none()

        if curso_up:
            curso_up.titulo = curso.titulo
            curso_up.aulas = curso.aulas
            curso_up = curso.horas

            await sesssion.commit()

            return curso_up

        else:
            raise HTTPException(detail='Curso não encontrado.',
                                status_code=status.HTTP_404_NOT_FOUND)


# Delete curso


@router.delete('/{curso_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db as sesssion:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await sesssion.execute(query)
        curso_del = result.scalar_one_or_none()

        if curso_del:
            await sesssion.delete(curso_del)
            await sesssion.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)

        else:
            raise HTTPException(detail='Curso não encontrado.',
                                status_code=status.HTTP_404_NOT_FOUND)
