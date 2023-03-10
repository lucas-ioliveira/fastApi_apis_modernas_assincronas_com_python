from fastapi import FastAPI

# Para responses
from fastapi.responses import JSONResponse
from fastapi import Response

# Para tratamento de erros.
from fastapi import HTTPException
from fastapi import status

# Para parâmetros
from fastapi import Path

# Arquivo interno
from models import Curso
from models import cursos

app = FastAPI(
    title='API de Cursos da Geek University',
    version='0.0.1',
    description='Uma api para estudos do FastApi'
)


# Lê todos.
@app.get('/cursos', description='Retorna todos os cursos ou uma lista vazia.')
async def get_cursos():
    return cursos


# Lê um dado específico.
@app.get('/curso/{curso_id}', description='o ID do curso deve ser números inteiros.')
async def get_curso(curso_id: int):
    try:
        id_curso = cursos[curso_id]
        return id_curso

    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado.')


# Inserindo dados.
@app.post('/curso', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    next_id: int = len(cursos) + 1
    curso.id = next_id
    cursos.append(curso)
    return curso


# Atualiza dados
@app.put('/curso/{curso_id}')
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id

        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado.')


# Deletar dados
@app.delete('/curso/{curso_id}')
async def delete_curso(curso_id: int):
    if curso_id in cursos:
        del cursos[curso_id]

        return f'Deletado {Response(status_code=status.HTTP_204_NO_CONTENT)}'

    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado.')


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)
