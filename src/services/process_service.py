import json
import re
from workers.crew_worker import CrewWorker
from services.crew_service import CrewService
from utils.json_utils import JsonUtils

class ProcessService:
    def __init__(self, crew_service: CrewService):
        """
        Initializes ProcessService with an instance of CrewService.
        
        :param crew_service: CrewService instance used to create the Crew.
        """
        self.crew_service = crew_service

    def process_principal(self, content: str, agent_path: str, example_path: str):
        """
        """
        try:
            example = self._load_json(example_path)
            if not example:
                raise ValueError("Field 'example' not found in the JSON file.")
            
            processed_text = self.process_principal_text(agent_path, {"content": content, "example": example })

            print(f"Terminou o processo principal")

            return processed_text
        
        except Exception as e:
            print(f"Error processing example from JSON: {e}")
            return None
    
    def process_script(self, content: str, agent_path: str, example_path: str):
        """
        """
        try:
            example = self._load_json(example_path)
            if not example:
                raise ValueError("Field 'example' not found in the JSON file.")
            
            processed_text = self.process_principal_text(agent_path, {"content": content, "example": example })

            print(f"Terminou o processo de geração de script")

            return processed_text
        
        except Exception as e:
            print(f"Error processing example from JSON: {e}")
            return None

    def process_list(self, content: str, agent_path: str, example_path: str):
        """
        """
        try:
            example = self._load_json(example_path)
            if not example:
                raise ValueError("Field 'example' not found in the JSON file.")
            
            processed_text = self.process_principal_text(agent_path, {"content": content, "example": example })

            print(f"Terminou o processo de geração de exercicio")

            return processed_text
        
        except Exception as e:
            print(f"Error processing example from JSON: {e}")
            return None

    def process_analyst(self, content: str, agent_path: str, example_path: str):
        """
        """
        try:
            example = self._load_json(example_path)
            if not example:
                raise ValueError("Field 'example' not found in the JSON file.")
            
            processed_text = self.process_principal_text(agent_path, {"content": content, "example": example })

            print(f"Terminou o processo da analise do script")

            return processed_text
        
        except Exception as e:
            print(f"Error processing example from JSON: {e}")
            return None

    def process_study_plan(self, content: str, agent_path: str, example_path: str):
        """
        """
        try:
            example = self._load_json(example_path)
            if not example:
                raise ValueError("Field 'example' not found in the JSON file.")
            
            processed_text = self.process_principal_text(agent_path, {"content": content, "example": example })

            print(f"Terminou o processo de plano de estudos")

            return processed_text
        
        except Exception as e:
            print(f"Error processing example from JSON: {e}")
            return None


    def process_principal_text(self, json_path: str, inputs: dict) -> dict:
        """
        Processes text using CrewService to create a Crew and CrewWorker for execution.

        :param json_path: Path to the JSON containing the Agent, Task, and Crew configuration.
        :param prospect_id: ID of the prospect to be added to the result.
        :return: A dictionary containing the processed result and the prospect ID.
        """
        try:
            crew = self.crew_service.create_from_json(json_path)
            if not crew:
                raise ValueError("Error creating Crew from JSON.")

            crew_worker = CrewWorker(crew=crew)
            result = crew_worker.process(inputs=inputs)

            return result.raw

        except Exception as e:
            print(f"Error processing text: {e}")
            raise e

    def _load_json(self, path: str) -> dict:
        """
        Helper method to load a JSON file.

        :param path: Path to the JSON file.
        :return: Loaded JSON as a dictionary.
        """
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def is_json(self, string):
        try:
            # Tenta fazer o parsing da string como JSON
            json.loads(string)
        except ValueError:
            # Se der erro, não é um JSON válido
            return False
        return True

    def _convert_result_to_string(self, result) -> str:
        """
        Helper method to convert the processing result to a string.

        :param result: The result to convert.
        :return: Result as a string.
        """
        if isinstance(result, dict):
            first_key = next(iter(result))
            return str(result[first_key])
        elif isinstance(result, str):
            return result
        return str(result)