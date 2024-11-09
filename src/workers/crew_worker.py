from crewai import Crew

class CrewWorker:
    def __init__(self, crew: Crew):
        """
        Initializes CrewWorker with a Crew instance.
        """
        self.crew = crew

    def process(self, inputs: dict):
        """
        Function to kick off the task using the provided content and example.

        :param inputs: A dictionary containing the inputs for the processing task.
        :return: The result of the process or None if an error occurs.
        """
        try:
            # Start the crew process
            result = self.crew.kickoff(inputs=inputs)
            return result
        except Exception as e:
            print(f"Error during processing with Crew: {e}")
            return None