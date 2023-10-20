from django.views.generic import ListView

from django.contrib.auth.models import User

class UserListView(ListView):
    model = User
    template_name = 'home/user_list.html'
    context_object_name = 'users'