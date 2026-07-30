import pytest
from datetime import datetime, timedelta
from solution import Meeting, MeetingService



"""
The method returns a list of upcoming meetings based on the following criteria:

1. Future meetings (e.g., tomorrow at 12:00) -> Included in the list.
2. Past meetings (e.g., yesterday) -> Excluded from the list.
3. Boundary condition (e.g., 5 minutes ago) -> Included in the list (ongoing meetings).

"""


def test_should_return_only_future_and_ongoing_meetings():
    current_system_time = datetime.now()
    m_past = Meeting(1, "Old meeting", current_system_time - timedelta(days=2))
    m_ongoing = Meeting(2, "Ongoing", current_system_time + timedelta(seconds =10))
    m_future = Meeting(3, "Future", current_system_time + timedelta(days=1))


    meetings = [m_past,m_ongoing, m_future]

    meeting_service= MeetingService(meetings)
    result = meeting_service.get_upcoming_meeting()

    assert result == [m_ongoing, m_future]

