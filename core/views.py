from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.views import generic

from .forms import GenerateRandomUserForm
from .tasks import create_random_user_accounts
  
class  GenerateRandomUserForm(FormView):
        template_name = 'generate_random_users.html'
        form_class = GenerateRandomUserForm

def form_valid(self, form):
    total = form.cleaned_data.get('total')                                                                                            
    create_random_user_accounts.delay(total)
    messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
    return redirect('users_list')

class  UsersListView(generic.ListView):
     template_name = 'users/generate_random_users.html'
     model = User

def get_queryset(self):
    return User.objects.all()