from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

from .views import SignUp

urlpatterns = [
    path("", views.home, name="home"),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', SignUp.as_view(), name='signup')
]