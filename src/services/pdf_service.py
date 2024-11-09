from services.base_service import BaseService
from utils.file_utils import save_file

class PDFService(BaseService):
    async def process(self, file):
        saved_path = await save_file(file, "pdfs")
        # Processamento específico de PDF
        return {"path": saved_path, "file_type": "PDF"}