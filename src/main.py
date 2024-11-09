from fastapi import FastAPI, UploadFile, File, Form
from services.pdf_service import PDFService
from services.image_service import ImageService
from services.text_service import TextService

app = FastAPI()

# Instanciando serviços
pdf_service = PDFService()
image_service = ImageService()
text_service = TextService()

@app.post("/upload/pdf")
async def upload_pdf(file: UploadFile = File(...)):
    result = await pdf_service.process(file)
    return {"message": "PDF processed", "details": result}

@app.post("/upload/image")
async def upload_image(file: UploadFile = File(...)):
    result = await image_service.process(file)
    return {"message": "Image processed", "details": result}

@app.post("/upload/text")
async def upload_text(content: str = Form(...)):
    result = text_service.process(content)
    return {"message": "Text pro cessed", "details": result}