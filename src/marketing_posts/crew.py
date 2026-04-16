from dotenv import load_dotenv
load_dotenv()

from typing import List
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from pydantic import BaseModel, Field

# CrewAI native Ollama integration
llm = LLM(
    model="ollama/llama3",
    base_url="http://127.0.0.1:11434"
)

# Web search tool
search_tool = SerperDevTool()


class MarketStrategy(BaseModel):
    name: str = Field(..., description="Name of the market strategy")
    tactics: List[str] = Field(..., description="List of tactics")
    channels: List[str] = Field(..., description="Marketing channels")
    KPIs: List[str] = Field(..., description="Key performance indicators")


class CampaignIdea(BaseModel):
    name: str = Field(..., description="Campaign name")
    description: str = Field(..., description="Campaign description")
    audience: str = Field(..., description="Target audience")
    channel: str = Field(..., description="Marketing channel")


class Copy(BaseModel):
    title: str = Field(..., description="Copy title")
    body: str = Field(..., description="Copy body")


@CrewBase
class MarketingPostsCrew():

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # Research Agent (with web search)
    @agent
    def lead_market_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["lead_market_analyst"],
            llm=llm,
            tools=[search_tool],
            verbose=True
        )

    # Strategy Agent
    @agent
    def chief_marketing_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config["chief_marketing_strategist"],
            llm=llm,
            verbose=True
        )

    # Content Creator
    @agent
    def creative_content_creator(self) -> Agent:
        return Agent(
            config=self.agents_config["creative_content_creator"],
            llm=llm,
            verbose=True
        )

    # Growth Hacker Agent
    @agent
    def growth_hacker(self) -> Agent:
        return Agent(
            config=self.agents_config["growth_hacker"],
            llm=llm,
            verbose=True
        )

    # TASKS

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_task"],
            agent=self.lead_market_analyst()
        )

    @task
    def project_understanding_task(self) -> Task:
        return Task(
            config=self.tasks_config["project_understanding_task"],
            agent=self.chief_marketing_strategist(),
            context=[self.research_task()]
        )

    @task
    def marketing_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config["marketing_strategy_task"],
            agent=self.chief_marketing_strategist(),
            context=[self.research_task(), self.project_understanding_task()]
        )

    @task
    def growth_plan_task(self) -> Task:
        return Task(
            config=self.tasks_config["growth_plan_task"],
            agent=self.growth_hacker(),
            context=[self.marketing_strategy_task()]
        )

    @task
    def campaign_idea_task(self) -> Task:
        return Task(
            config=self.tasks_config["campaign_idea_task"],
            agent=self.creative_content_creator(),
            context=[self.marketing_strategy_task(), self.growth_plan_task()]
        )

    @task
    def copy_creation_task(self) -> Task:
        return Task(
            config=self.tasks_config["copy_creation_task"],
            agent=self.creative_content_creator(),
            context=[self.campaign_idea_task()]
        )

    @task
    def final_report_task(self) -> Task:
        return Task(
            config=self.tasks_config["final_report_task"],
            agent=self.chief_marketing_strategist(),
            context=[
                self.research_task(),
                self.project_understanding_task(),
                self.marketing_strategy_task(),
                self.growth_plan_task(),
                self.campaign_idea_task(),
                self.copy_creation_task()
            ]
        )

    # CREW PIPELINE
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=[
                self.research_task(),
                self.project_understanding_task(),
                self.marketing_strategy_task(),
                self.growth_plan_task(),
                self.campaign_idea_task(),
                self.copy_creation_task(),
                self.final_report_task()
            ],
            process=Process.sequential,
            verbose=True
        )