import json
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

    def process_prospect_info(self, content: str, agent_path: str, example_path: str, prospect_id: str):
        """
        Processes the prospect information by reading an example JSON and using the CrewService 
        to execute text processing.

        :param content: Content to be processed.
        :param agent_path: Path to the agent configuration.
        :param example_path: Path to the example JSON file.
        :param prospect_id: ID of the prospect.
        :return: Processed result as a dictionary or None if an error occurs.
        """
        try:
            example = self._load_json(example_path)
            if not example:
                raise ValueError("Field 'example' not found in the JSON file.")

            processed_text = self.process_text(agent_path, prospect_id, {"content": content, "example": example})
            return json.loads(processed_text)

        except Exception as e:
            print(f"Error processing example from JSON: {e}")
            return None
    
    def process_principal(self, content: str, agent_path: str, example_path: str, prospect_id: str):
        """
        """
        try:
            example = self._load_json(example_path)
            if not example:
                raise ValueError("Field 'example' not found in the JSON file.")
            
            processed_text = self.process_principal_text(agent_path, {"content": content, "example": example})
            return json.loads(processed_text)
        
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

            if not result:
                raise ValueError("CrewWorker processing failed, empty result.")

            if not JsonUtils.is_json(result):
                raise ValueError("Agent did not create a valid JSON.")

            return JsonUtils.add_to_json(result)

        except Exception as e:
            print(f"Error processing text: {e}")
            raise e


    def process_table_conversion(self, page: str, agent_path: str, example_path: str, overlap: str):
        """
        Processes a table by reading an example JSON and using the CrewService to process the table.

        :param page: Content of the table.
        :param agent_path: Path to the agent configuration.
        :param example_path: Path to the example JSON file.
        :param overlap: Overlapping text to be processed.
        :return: Processed result as a string or None if an error occurs.
        """
        try:
            example = self._load_json(example_path)
            if not example:
                raise ValueError("Field 'example' not found in the JSON file.")
            
            converted_text = self.process_table(agent_path, {"content": overlap, "table": page, "example": example.get("converted_text", None)})
            return converted_text

        except Exception as e:
            print(f"Error processing table from JSON: {e}")
            return None

    def process_text(self, json_path: str, prospect_id: str, inputs: dict) -> dict:
        """
        Processes text using CrewService to create a Crew and CrewWorker for execution.

        :param json_path: Path to the JSON containing the Agent, Task, and Crew configuration.
        :param prospect_id: ID of the prospect to be added to the result.
        :param inputs: Input dictionary with content and example data.
        :return: A dictionary containing the processed result and the prospect ID.
        """
        try:
            crew = self.crew_service.create_from_json(json_path)
            if not crew:
                raise ValueError("Error creating Crew from JSON.")

            crew_worker = CrewWorker(crew=crew)
            result = crew_worker.process(inputs=inputs)

            if not result:
                raise ValueError("CrewWorker processing failed, empty result.")

            if not JsonUtils.is_json(result):
                raise ValueError("Agent did not create a valid JSON.")

            return JsonUtils.add_to_json(result, {"id": prospect_id})

        except Exception as e:
            print(f"Error processing text: {e}")
            raise e

    def process_table(self, json_path: str, inputs: dict) -> str:
        """
        Processes a table using CrewService to create a Crew and CrewWorker for execution.

        :param json_path: Path to the JSON containing the Agent, Task, and Crew configuration.
        :param inputs: Input dictionary with content and table data.
        :return: Processed result as a string.
        """
        try:
            crew = self.crew_service.create_from_json(json_path)
            if not crew:
                raise ValueError("Error creating Crew from JSON.")

            crew_worker = CrewWorker(crew=crew)
            result = crew_worker.process(inputs=inputs)

            return self._convert_result_to_string(result)

        except Exception as e:
            print(f"Error processing table: {e}")
            raise e

    def _load_json(self, path: str) -> dict:
        """
        Helper method to load a JSON file.

        :param path: Path to the JSON file.
        :return: Loaded JSON as a dictionary.
        """
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)

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