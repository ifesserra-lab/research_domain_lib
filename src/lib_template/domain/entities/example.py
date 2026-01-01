from pydantic import Field
from libbase.domain.entities.base import BaseEntity

class Example(BaseEntity):
    name: str = Field(..., description="The name of the example entity")
    description: str | None = Field(None, description="A description of the example entity")
