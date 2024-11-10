import os
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from services.pdf_service import PDFService
from services.image_service import ImageService
from services.text_service import TextService
from services.crew_service import CrewService
from services.process_service import ProcessService

os.environ["HUGGINGFACE_TOKEN"] = "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"
os.environ["GROQ_API_KEY"] = "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"

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
        print("Iniciando o processamento do arquivo PDF.")
        
        result = await pdf_service.process(file)
        print("Resultado obtido do serviço PDF:", result)
        
        # Verifica se o campo "content" e "text" existe
        if not result.get("content") or not result["content"][0].get("text"):
            print("Erro: Campo 'text' não encontrado em 'content'.")
            raise HTTPException(status_code=400, detail="Texto não encontrado no conteúdo do PDF.")

        # Caminho para os arquivos JSON
        agent_path = os.path.join("jsons", "agents", "theme_subtheme.json")
        example_path = os.path.join("jsons", "examples", "theme_subtheme.json")
        
        print("Processando o texto com CrewAI.")
        
        # Processa o texto com CrewAI
        processed_data = process_service.process_principal(
            content=result["content"][0]["text"],
            agent_path=agent_path,
            example_path=example_path
        )

        print("Processamento concluído com sucesso.")
        return {"message": "Image processed", "details": processed_data } 
    
    except HTTPException as http_exc:
        print("Erro HTTP:", http_exc.detail)
        raise http_exc

    except Exception as e:
        print("Erro ao processar o PDF:", str(e))
        raise HTTPException(status_code=500, detail="Erro interno no processamento do PDF.")
    

@app.post("/upload/image")
async def upload_image(file: UploadFile = File(...)):
    result = await image_service.process(file)
    return {"message": "Image processed", "details": result}

@app.post("/upload/text")
async def upload_text(content: str = Form(...)):
    result = text_service.process(content)
    return {"message": "Text pro cessed", "details": result}