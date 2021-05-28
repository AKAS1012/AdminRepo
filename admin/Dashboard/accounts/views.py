from django.views.generic import CreateView
from django.urls import reverse_lazy
from . import forms

class Signup(CreateView):
    form_class = forms.UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/Signup.html'



