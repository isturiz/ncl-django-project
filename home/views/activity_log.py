from django.views.generic import ListView
from home.models import ActivityLog

from django.http import HttpResponse
from django.views import View


class ActivityLog_ListView(ListView):
    model = ActivityLog
    template_name = 'home/activity_log_list.html'
    context_object_name = 'activity_logs'
    ordering = ['-timestamp']

class LogActivity_View(View):
    def post(self, request, action):
        if request.user.is_authenticated:
            ActivityLog.objects.create(user=request.user, action=action)
        return HttpResponse(status=200)
    
from django.shortcuts import render
from django.contrib.admin.models import LogEntry
from django.contrib.contenttypes.models import ContentType

def action_history_view(request):
    log_entries = LogEntry.objects.all().select_related('user').order_by('-action_time')
    return render(request, 'home/action_history.html', {'log_entries': log_entries})
