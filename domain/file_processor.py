import csv
import os
from fastapi import UploadFile, HTTPException, status

class FileProcessor:
    """Manager of files and folders processor."""

    def __init__(self):
        self.file_path = 'data/seu_file.csv'
        self.directory = 'data'

    def create_files(self):
        if not os.path.exists(self.file_path):
            os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['conta', 'agencia', 'teste', 'valor'])
                return {"Mensagem": f"Arquivo {self.file_path} criado com sucesso!"}
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Arquivo já existe")

    async def upload_file(self, file: UploadFile):
        if file.filename.endswith('.csv'):
            try:

                content = await file.read()
                decoded_file = content.decode('utf-8').splitlines()

                csv_reader = csv.DictReader(decoded_file)
                for row in csv_reader:
                    print(row)
                return {"mensagem": f"Arquivo {file.filename} processado com sucesso"}
            except Exception as e:
                raise HTTPException(
                    status_code=status.HTTP_406_NOT_ACCEPTABLE,
                    detail=f"Falha ao processar o arquivo CSV: {str(e)}"
                )
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="O arquivo deve ser do tipo .csv"
            )
    async def add_data_to_file(self, data: dict):
        # add data to file created
        # :param data: account data history
        # :return: error or sucess message

        if os.path.exists(self.file_path):
            with open(self.file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([data["conta"], data["agencia"], data["texto"], data["valor"]])
                return {"mensagem": f"Dados inseritos com sucesso: {data}"}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Arquivo inexistente, por favor acessar"
                                    "a rota de criar o arquivo")

