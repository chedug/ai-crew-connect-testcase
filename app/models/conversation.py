from pydantic import BaseModel, Field
from app.utils.enum import Roles


class Message(BaseModel):
    input: str = Field("", description="User input")
    output: str = Field("", description="Agent response (optional)")


class ConversationData(BaseModel):
    role: Roles = Field(Roles.SALES_MANAGER, description="Role of the agent")
    conversation: list[Message] = Field("", description="List of conversation messages")
