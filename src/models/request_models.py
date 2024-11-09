from pydantic import BaseModel

class TextRequest(BaseModel):
    content: str
