from .home import HomePageView

# Change add -> Create

from .student import Student_ListView, Student_CreateView, Student_UpdateView, StudentGraph_View
from .teacher import TeacherListView, TeacherAddView, TeacherUpdateView
from .lesson import LessonListView, LessonCreateView, LessonUpdateView
from .subscription import SubscriptionListView, SubscriptionCreateView, SubscriptionUpdateView
from .calendar import CalendarView, EventCreateView, EventUpdateView, EventLessonUpdateView
from .finance import FinanceView
from .user import UserListView
from .payments import PaymentListView, PaymentCreateView, PaymentUpdateView

from .lesson import load_subscriptions


