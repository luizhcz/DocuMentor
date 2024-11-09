from crewai import Crew, Agent, Task

def extract_context(text):    
    # Pseudocódigo para processar o texto:
    main_topic = "Identificar o tema principal do texto"
    subtopics = ["Extrair sub-tópicos 1", "Extrair sub-tópicos 2"] 
    important_details = ["Detalhe 1 relevante", "Detalhe 2 relevante"]
    
    return {
        "main_topic": main_topic,
        "subtopics": subtopics,
        "important_details": important_details
    }

# Passo 2: Defina o Agente
class TextAnalyzerAgent(Agent):
    def __init__(self):
        super().__init__("TextAnalyzerAgent")

    def handle_task(self, task):
        # Executa a tarefa de análise de contexto
        text = task.data.get("text")
        analysis_result = extract_context(text)
        return analysis_result

# Passo 3: Crie a Tarefa para o Agente
class AnalyzeTextTask(Task):
    def __init__(self, text):
        super().__init__("AnalyzeTextTask")
        self.data = {"text": text}

# Passo 4: Configure a Equipe (Crew) e Execute
# Crie uma equipe e adicione o agente
crew = Crew("TextAnalysisCrew")
text_analyzer = TextAnalyzerAgent()
crew.add_agent(text_analyzer)

# Texto de exemplo
input_text = "Seu texto de entrada aqui para análise."

# Crie a tarefa e execute
task = AnalyzeTextTask(input_text)
result = crew.run(task)

# Exiba o resultado
print(result)
