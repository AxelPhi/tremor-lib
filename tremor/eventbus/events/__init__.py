from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BaseEvent(BaseModel):
    source: str
    timestamp: Optional[datetime] = datetime.utcnow()


class ChatEvent(BaseEvent):
    msg: str
    sender: str
