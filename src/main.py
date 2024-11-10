import os
import json
import hashlib
import uuid
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
from services.pdf_service import PDFService
from services.image_service import ImageService
from services.text_service import TextService
from services.crew_service import CrewService
from services.process_service import ProcessService
from services.generator_service import GeneratorService

os.environ["HUGGINGFACE_TOKEN"] = "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"
os.environ["GROQ_API_KEY"] = "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"

app = FastAPI()

# Instanciando serviços
pdf_service = PDFService()
image_service = ImageService()
text_service = TextService()
crew_service = CrewService()
process_service = ProcessService(crew_service=crew_service)
generator_service = GeneratorService()

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

        # Caminho para os arquivos JSON
        agent_secund_path = os.path.join("jsons", "agents", "script_generator.json")
        example_secund_path = os.path.join("jsons", "examples", "script_example.json")

        # Processa o texto com CrewAI
        script_tutor = process_service.process_script(
            content=processed_data,
            agent_path=agent_secund_path,
            example_path=example_secund_path
        )

        # Caminho para os arquivos JSON
        agent_list_ex_path = os.path.join("jsons", "agents", "list_ex_generator.json")
        example_list_ex_path = os.path.join("jsons", "examples", "list_ex_example.json")

        processed_data_list = process_service.process_list(
            content=script_tutor,
            agent_path=agent_list_ex_path,
            example_path=example_list_ex_path
        )

        # Caminho para os arquivos JSON
        agent_analyzer_path = os.path.join("jsons", "agents", "study_plan_content_analyzer.json")
        example_analyzer_path = os.path.join("jsons", "examples", "study_plan_content_analyzer.json")

        processed_data_analyst = process_service.process_analyst(
            content=script_tutor,
            agent_path=agent_analyzer_path,
            example_path=example_analyzer_path
        )

        # Caminho para os arquivos JSON
        agent_study_plan_path = os.path.join("jsons", "agents", "study_plan.json")
        example_study_plan_path = os.path.join("jsons", "examples", "study_plan.json")

        processed_data_study_plan = process_service.process_study_plan(
            content=processed_data_analyst,
            agent_path=agent_study_plan_path,
            example_path=example_study_plan_path
        )

        file_hash = str(uuid.uuid4())
        file_exercise = f"{file_hash}_exercise.pdf"
        file_study_plan = f"{file_hash}_plan.pdf"

        path1 = os.path.join("pdfs", file_exercise)
        path2 = os.path.join("pdfs", file_study_plan)

        generator_service.generate_pdf_from_markdown(processed_data_list, path1)
        generator_service.generate_pdf_from_markdown(processed_data_study_plan, path2)

        # Retorna o JSON mapeado
        return { "script": script_tutor, "exercise" : path1, "study_plan": path2 }
    
    except HTTPException as http_exc:
        print("Erro HTTP:", http_exc.detail)
        raise http_exc
    except json.JSONDecodeError:
        print("Erro: Dados retornados não são JSON válido.")
        raise HTTPException(status_code=500, detail="Erro no processamento do JSON.")
    except Exception as e:
        print("Erro inesperado:", str(e))
        raise HTTPException(status_code=500, detail="Erro no processamento do PDF.")
    

@app.post("/upload/image")
async def upload_image(file: UploadFile = File(...)):
    result = await image_service.process(file)
    return {"message": "Image processed", "details": result}

@app.post("/upload/text")
async def upload_text(content: str = Form(...)):
    result = text_service.process(content)
    return {"message": "Text pro cessed", "details": result}