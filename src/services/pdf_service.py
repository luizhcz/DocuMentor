from typing import Any
from repositories.pdf_repository import PdfRepository
from io import BytesIO
from PyPDF2 import PdfReader

class PdfService:
    def __init__(self, repository: PdfRepository = None):
        # Injeção de dependência: permitindo mockar o repositório em testes, se necessário
        self.repository = repository or PdfRepository()

    async def process_pdf(self, file: Any) -> str:
        # Lê o arquivo PDF utilizando o repositório
        pdf_bytes = await self.repository.read_file(file)
        
        # Processa o PDF e extrai o texto
        return self.extract_text_from_pdf(pdf_bytes)

    def extract_text_from_pdf(self, pdf_bytes: bytes) -> str:
        # Utiliza PyPDF2 para extrair texto do PDF
        pdf_reader = PdfReader(BytesIO(pdf_bytes))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
        return text