from typing import Optional
from pydantic import BaseModel


class Location(BaseModel):
    city: str
    country: str = 'us'
    state: Optional[str] = None
