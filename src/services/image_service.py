from services.base_service import BaseService
from utils.file_utils import save_file

class ImageService(BaseService):
    async def process(self, file):
        saved_path = await save_file(file, "images")
        # Processamento específico de imagem
        return {"path": saved_path, "file_type": "Image"}
