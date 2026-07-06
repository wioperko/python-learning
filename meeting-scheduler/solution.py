from dataclasses import dataclass
from datetime import datetime, date, time
import pytz
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
    
    def __repr__(self):
        return f'Meeting(ID={self.meeting_id}, DATETIME={self.meeting_datetime}, DESCRIPTION={self.description})'
    
def main() -> None:
    m1 = Meeting(1, 'Project kickoff', datetime(2026, 7, 6, 23, 0, tzinfo=pytz.timezone('Europe/Warsaw')))
    m2 = Meeting(2, 'Team standup', datetime(2026, 8, 28, 10, 0, tzinfo=pytz.timezone('America/New_York')))
    m3 = Meeting(3, 'Client presentation', datetime(2026, 8, 28, 14, 0, tzinfo=pytz.timezone('Europe/London')))
    m4 = Meeting(4, 'Retrospective', datetime(2026, 8, 27, 15, 0, tzinfo=pytz.timezone('Asia/Tokyo')))
    m5 = Meeting(5, 'Team sync', datetime(2026, 8, 29, 11, 0, tzinfo=pytz.timezone('Australia/Sydney')))

    print(m1)
    print(m2)
    print(m3)
    print(m4)
    print(m5)

    print(m1.has_occurred)
    print(m1.is_today)
    print(m1.is_upcoming)


if __name__ =='__main__':
    main()