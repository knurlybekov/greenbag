from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
def home(request):
    return render(request, "home.html")

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class addpost(generic.CreateView):
    template_name = 'addpost.html'