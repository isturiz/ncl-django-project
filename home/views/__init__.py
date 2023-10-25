from .home import HomePageView

# Change add -> Create

from .student import Student_ListView, Student_CreateView, Student_UpdateView, StudentGraph_View
from .teacher import TeacherListView, TeacherAddView, TeacherUpdateView
from .lesson import LessonListView, LessonCreateView, LessonUpdateView
from .subscription import SubscriptionListView, SubscriptionCreateView, SubscriptionUpdateView
from .calendar import CalendarView, EventCreateView, EventUpdateView, EventLessonUpdateView
from .finance import FinanceView
from .user import UserListView

from .payments import Payment_ListView, Payment_CreateView, Payment_UpdateView

from .lesson_types import LessonTypes_ListView, LessonTypes_CreateView, LessonTypes_UpdateView
from .subscription_types import SubscriptionTypes_ListView, SubscriptionTypes_CreateView, SubscriptionTypes_UpdateView



from .lesson import load_subscriptions

from .activity_log import auditlog_view


