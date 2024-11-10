from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq

class CrewSetup:
    def __init__(self, model_name: str = "gpt-4o-mini", temperature: float = 0.1, max_execution_time: int = 999999):
        """
        Initializes the CrewSetup with default configurations for creating Agent, Task, and Crew.
        
        :param model_name: Name of the LLM model to be used in the Agent.
        :param temperature: Temperature setting for the LLM model.
        :param max_execution_time: Maximum execution time for the Agent, Task, and Crew.
        """
        self.model_name = model_name
        self.temperature = temperature
        self.max_execution_time = max_execution_time

    def create_agent(self, role: str, goal: str, backstory: str, verbose: bool = True, memory: bool = True, max_iter: int = 20) -> Agent:
        """
        Creates and returns an instance of Agent.

        :param role: Role of the agent.
        :param goal: Main goal of the agent.
        :param backstory: Agent's backstory for context.
        :param verbose: Determines if the agent should display additional information during processing.
        :param memory: Determines if the agent should maintain memory.
        :param max_iter: Maximum number of iterations the agent can perform.
        :return: Configured instance of Agent.
        """
        llm = ChatGroq(
            model_name=self.model_name, 
            temperature=self.temperature, 
            api_key='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')

        return Agent(
            role=role,
            goal=goal,
            verbose=verbose,
            memory=memory,
            max_iter=max_iter,
            backstory=backstory,
            llm=llm,
            max_execution_time=self.max_execution_time
        )

    def create_task(self, description: str, expected_output: str, agent: Agent) -> Task:
        """
        Creates and returns an instance of Task associated with the Agent.

        :param description: Description of the task.
        :param expected_output: Example of the expected output for the task.
        :param agent: Agent responsible for performing the task.
        :return: Configured instance of Task.
        """
        return Task(
            description=description,
            expected_output=expected_output,
            agent=agent,
            max_execution_time=self.max_execution_time,
            output_file='./search_text.json'
        )

    def create_crew(self, agents: list, tasks: list, verbose: bool) -> Crew:
        """
        Creates and returns an instance of Crew with configured agents and tasks.

        :param agents: List of agents that will be part of the Crew.
        :param tasks: List of tasks that the Crew will execute.
        :param verbose: Verbosity level during execution.
        :return: Configured instance of Crew.
        """
        return Crew(
            agents=agents,
            tasks=tasks,
            verbose=verbose,
            max_execution_time=self.max_execution_time
        )