from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BaseEvent(BaseModel):
    source: str
    timestamp: Optional[datetime] = datetime.utcnow()
    category: str = "base"


class ChatEvent(BaseEvent):
    msg: str
    sender: str
    category: str = "chat"
