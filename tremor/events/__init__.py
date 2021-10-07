from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import AnyUrl, BaseModel


class BaseEvent(BaseModel):
    source: str
    timestamp: Optional[datetime] = datetime.utcnow()
    category: str = "base"


class ChatEvent(BaseEvent):
    msg: str
    sender: str
    category: str = "chat"


class StreamStatus(str, Enum):
    unknown = "unknown"
    offline = "offline"
    online = "online"


class StreamStatusEvent(BaseEvent):
    status: StreamStatus = StreamStatus.unknown
    stream_url: AnyUrl = None
    category: str = "stream_status"
