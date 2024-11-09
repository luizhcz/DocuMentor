from services.base_service import BaseService

class TextService(BaseService):
    def process(self, content):
        # Processamento específico de texto
        return {"content_length": len(content), "file_type": "Text"}
