from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.post('/file/create_file')
async def create_file():
    return {'message': 'Arquivo criado com sucesso'}

@router.post('/file/add_data')
async def upload_file(file: UploadFile = File(...)):
    return {'message': 'Arquivo enviado com sucesso'}

@router.post('/file/add_data')
async def add_data(conta: str, agencia: str, texto: str, valor: float):
    data = {'conta': conta, 'agencia': agencia, 'texto': texto, 'valor': valor}
    return await FileProcessor().add_data_to_file()

@router.delete('/file/delete_data')
async def delete_data():
    return {'message': 'Dado removido com sucesso'}

@router.get('/file/list_files')
async def list_files():
    return {'message': 'Lista de dados'}
