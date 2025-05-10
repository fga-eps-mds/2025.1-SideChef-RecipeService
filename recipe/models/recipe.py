from pydantic import BaseModel, Field
from typing import Optional

class Item(BaseModel):
    name: str = Field(...)
    description: Optional[str] = None