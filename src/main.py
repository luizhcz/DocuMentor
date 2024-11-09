import os
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from services.pdf_service import PDFService
from services.image_service import ImageService
from services.text_service import TextService
from services.crew_service import CrewService
from services.process_service import ProcessService

app = FastAPI()

# Instanciando serviços
pdf_service = PDFService()
image_service = ImageService()
text_service = TextService()
crew_service = CrewService()
process_service = ProcessService(crew_service=crew_service)

@app.post("/upload/pdf")
async def upload_pdf(file: UploadFile = File(...)):

    try:
        result = await pdf_service.process(file)

        #Chamar CrewAI
        agent_path = os.path.join("jsons", "agent", "get_info_prospect.json")
        example_path = os.path.join("jsons", "example", "get_info_prospect.json")

        return result 

        # Process the text with CrewAI
        processed_data = process_service.process_principal_text(
            content=data.text,
            agent_path=agent_path,
            example_path=example_path
        )

        return {"message": "PDF processed", "details": result }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    #Extrair pdf
    

@app.post("/upload/image")
async def upload_image(file: UploadFile = File(...)):
    result = await image_service.process(file)
    return {"message": "Image processed", "details": result}

@app.post("/upload/text")
async def upload_text(content: str = Form(...)):
    result = text_service.process(content)
    return {"message": "Text pro cessed", "details": result}