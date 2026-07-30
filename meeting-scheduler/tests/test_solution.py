import pytest
from datetime import datetime, timedelta
from solution import Meeting, MeetingService



"""
Rules for upcoming meetings:

- Meetings scheduled in the future are returned.
- Meetings that have already finished are excluded.
- Meetings that are currently in progress are included.
"""


def test_should_return_only_future_and_ongoing_meetings():
    current_system_time = datetime.now()
    m1 = Meeting(1, "Old meeting", current_system_time - timedelta(days=2))
    m2 = Meeting(2, "Ongoing", current_system_time + timedelta(seconds =10))
    m3 = Meeting(3, "Future", current_system_time + timedelta(days=1))


    meetings = [m1,m2, m3]

    meeting_service= MeetingService(meetings)
    result = meeting_service.get_upcoming_meeting()

    assert result == [m2, m3]


def test_should_return_meetings_sorted_by_date():
    current_sys_time = datetime.now()

    m1 = Meeting(1,'First',current_sys_time + timedelta(hours=2))
    m2 = Meeting(2, 'Second', current_sys_time + timedelta(seconds=20))
    m3 = Meeting(3, "Third", current_sys_time + timedelta(days=1))

    meetings =[m1, m2, m3]

    meeting_service = MeetingService(meetings)
    result = meeting_service.get_upcoming_meeting()

    assert result == [m2, m1, m3]