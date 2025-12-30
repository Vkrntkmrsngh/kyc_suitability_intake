from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task, tool

from crewai_tools import SerperDevTool
from kyc_suitability_intake.tools.kyc_completeness_tool import KycCompletenessTool

@CrewBase
class KycSuitabilityIntakeCrew:
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # --- Tools ---
    @tool
    def serper_search_tool(self):
        # Keep results small so the agent stays focused
        return SerperDevTool(n_results=3)

    @tool
    def kyc_completeness_tool(self):
        return KycCompletenessTool()

    # --- Agents ---
    @agent
    def intake_extractor(self) -> Agent:
        return Agent(config=self.agents_config["intake_extractor"], verbose=True)

    @agent
    def risk_profiler(self) -> Agent:
        return Agent(config=self.agents_config["risk_profiler"], verbose=True)

    @agent
    def advisor_summary_writer(self) -> Agent:
        return Agent(config=self.agents_config["advisor_summary_writer"], verbose=True)

    # --- Tasks ---
    @task
    def extract_profile_task(self) -> Task:
        return Task(config=self.tasks_config["extract_profile_task"])

    @task
    def risk_profile_task(self) -> Task:
        return Task(config=self.tasks_config["risk_profile_task"])

    @task
    def advisor_summary_task(self) -> Task:
        return Task(config=self.tasks_config["advisor_summary_task"])

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )