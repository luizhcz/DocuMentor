import json
from workers.crew_setup import CrewSetup

class CrewService:
    def __init__(self):
        """
        Initializes the CrewService with a CrewSetup instance.
        """
        self.crew_setup = None

    def create_from_json(self, path: str):
        """
        Loads a JSON file containing the definitions of Agent, Task, and Crew, and creates them.

        :param path: Path to the JSON file with configuration parameters.
        :return: Crew instance created from the configurations, or None if an error occurs.
        """
        try:
            # Load the JSON file
            with open(path, 'r', encoding='utf-8') as file:
                config = json.load(file)

            # Model configurations
            model_config = config.get("model_config", {})
            model_name = model_config.get("model_name", "gpt-4o-mini")
            temperature = model_config.get("temperature", 0.1)
            max_execution_time = model_config.get("max_execution_time", 999999)

            # Initialize CrewSetup with model configurations
            self.crew_setup = CrewSetup(
                model_name=model_name,
                temperature=temperature,
                max_execution_time=max_execution_time
            )

            # Create the Agent from the JSON parameters
            agent_config = config.get("agent", {})
            agent = self.crew_setup.create_agent(
                role=agent_config.get("role", "Default Role"),
                goal=agent_config.get("goal", "Default Goal"),
                backstory=agent_config.get("backstory", ""),
                verbose=agent_config.get("verbose", True),
                memory=agent_config.get("memory", True),
                max_iter=agent_config.get("max_iter", 20)
            )

            # Create the Task from the JSON parameters
            task_config = config.get("task", {})
            task = self.crew_setup.create_task(
                description=task_config.get("description", "Default description"),
                expected_output=task_config.get("expected_output", "Default output"),
                agent=agent
            )

            # Create the Crew from the JSON parameters
            crew_config = config.get("crew", {})
            crew = self.crew_setup.create_crew(
                agents=[agent],
                tasks=[task],
                verbose=crew_config.get("verbose", 2)
            )

            return crew

        except Exception as e:
            print(f"Error creating Crew from JSON: {e}")
            return None