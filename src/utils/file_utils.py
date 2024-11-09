import os
from fastapi import UploadFile

async def save_file(file: UploadFile, folder: str):
    file_location = f"{folder}/{file.filename}"
    os.makedirs(folder, exist_ok=True)
    with open(file_location, "wb") as buffer:
        buffer.write(await file.read())
    return file_location
