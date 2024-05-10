from pydantic import BaseModel, Field
from app.utils.enum import Roles


class SampleData(BaseModel):
    input: str = Field("Hello bla-bla-bla", description="User input")
    output: str = Field("bla-bla-bla", description="Agent response")


class TrainingData(BaseModel):
    role: Roles = Field(Roles.SALES_MANAGER, description="Role of the agent")
    sample_data: list[SampleData] = Field("sample data", description="List of training examples")
