import os
from pathlib import Path
from llama_parse import LlamaParse
from services.base_service import BaseService
from utils.file_utils import save_file
import nest_asyncio

# Aplica nest_asyncio para permitir chamadas assíncronas em Jupyter ou outros ambientes que necessitem
nest_asyncio.apply()


class PDFService(BaseService):
    def __init__(self):
        # Obtém a chave de API do LlamaParse a partir das variáveis de ambiente
        api_key = os.getenv("LLAMA_CLOUD_API_KEY", "llx-a1AVsj4dX26LSMoOIn1K8uUruRXgxqhMr86Pqt8evFL14rRO")
        if not api_key:
            raise ValueError("A chave de API do LlamaParse não está configurada.")
        
        # Configura o parser do LlamaParse
        self.parser = LlamaParse(
            api_key=api_key,
            result_type="markdown",  # Define o tipo de resultado como markdown
            #num_workers=4,           # Número de workers para processamento paralelo
            verbose=True,
            language="pt"            # Define o idioma como português
        )

    async def process(self, file):
        # Salva o arquivo PDF recebido
        saved_path = await save_file(file, "pdfs")
        
        # Processa o PDF utilizando o LlamaParse de maneira assíncrona
        documents = await self.parser.aload_data(saved_path)
        
        # Extrai o conteúdo em formato Markdown
        content_markdown = [doc.to_dict() for doc in documents]
        
        return {"content": content_markdown}