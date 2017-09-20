from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.edit import FormView
from django.shortcuts import redirect

from .forms import GenerateRandomUserForm
from .tasks import create_random_user_accounts

class  GenerateRandomUserForm(FormView):
	template_name = 'generate_random_users.html'
	form_class = GenerateRandomUserForm

	def form_valid(self, form):
		total = form.cleaned_data.get ('total')
		create_random_user_accounts.delay(total)
		messages.success (self.request, 'Estamos generando tu usuaruio aleatorio! Espera un momento y refresca esta pagina.')
		return redirect ('users_list')
		
