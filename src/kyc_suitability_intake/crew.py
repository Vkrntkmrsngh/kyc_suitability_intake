from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class KycSuitabilityIntakeCrew:
    """KYC/Suitability intake crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def intake_extractor(self) -> Agent:
        return Agent(
            config=self.agents_config["intake_extractor"],  # type: ignore[index]
            verbose=True
        )

    @agent
    def risk_profiler(self) -> Agent:
        return Agent(
            config=self.agents_config["risk_profiler"],  # type: ignore[index]
            verbose=True
        )

    @agent
    def advisor_summary_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["advisor_summary_writer"],  # type: ignore[index]
            verbose=True
        )

    @task
    def extract_profile_task(self) -> Task:
        return Task(
            config=self.tasks_config["extract_profile_task"]  # type: ignore[index]
        )

    @task
    def risk_profile_task(self) -> Task:
        return Task(
            config=self.tasks_config["risk_profile_task"]  # type: ignore[index]
        )

    @task
    def advisor_summary_task(self) -> Task:
        return Task(
            config=self.tasks_config["advisor_summary_task"]  # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,   # auto-collected by @agent
            tasks=self.tasks,     # auto-collected by @task
            process=Process.sequential,
            verbose=True)