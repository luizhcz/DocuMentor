from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from services.pdf_service import PdfService

app = FastAPI()

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        # Chama o serviço para processar o PDF
        pdf_service = PdfService()
        text = await pdf_service.process_pdf(file)
        
        # Se o texto foi extraído com sucesso, retorna a resposta
        return {"filename": file.filename, "text": text[:500]}  # Limite de 500 caracteres

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ocorreu um erro: {str(e)}")
