from pydantic import BaseModel, Field


class Response(BaseModel):
    id: str | None = Field(None, description="Unique identifier for the response")
    role: str = Field(..., description="Role of the agent")
    conversation: list[dict[str, str]] = Field(..., description="List of conversation messages")
    generated_response: str = Field(..., description="Generated response from the agent")


class Training(BaseModel):
    role: str = Field(..., description="Role of the agent")
    messages: list[dict[str, str]] = Field(..., description="Training messages containing examples")
