from dataclasses import dataclass
from datetime import datetime, date, time
@dataclass
class Meeting:
    meeting_id: int
    description: str
    meeting_datetime: datetime

    @property
    def has_occurred(self) -> bool:
        return self.meeting_datetime < datetime.now(self.meeting_datetime.tzinfo)
    
    @property
    def is_today(self) -> bool:
        now = datetime.now(self.meeting_datetime.tzinfo)
        return self.meeting_datetime.date() == now.date()
    
    @property
    def is_upcoming(self) -> bool:
        return self.meeting_datetime > datetime.now(self.meeting_datetime.tzinfo)