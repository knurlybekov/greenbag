from audioop import reverse

from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CustomUserCreationForm, UserChangeForm
from .models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request, "home.html")


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))  # Redirect to login page after signup
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_profile(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'user_profile.html', {'user': user})

# class addpost(generic.CreateView):
#     template_name = 'addpost.html'


# def user_login(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         user = authenticate(request, username=email, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('profile')  # Redirect to a success page.
#         else:
#             return render(request, 'login.html', {'error': 'Invalid email or password'})
#     else:
#         return render(request, 'login.html')


def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_profile', user_id=request.user.id)  # Redirect to the profile page
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})