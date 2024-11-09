import os
import hashlib
from fastapi import UploadFile

async def save_file(file: UploadFile, folder: str):
    # Cria a pasta, se ainda não existir
    os.makedirs(folder, exist_ok=True)
    
    # Lê o conteúdo do arquivo para gerar o hash
    content = await file.read()
    file_hash = hashlib.sha256(content).hexdigest()[:20]
    
    # Define o nome do arquivo com base no hash
    file_extension = file.filename.split('.')[-1]  # Obtém a extensão original do arquivo
    file_location = os.path.join(folder, f"{file_hash}.{file_extension}")
    
    # Salva o arquivo no caminho definido
    with open(file_location, "wb") as buffer:
        buffer.write(content)
    
    return file_location