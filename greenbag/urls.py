from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from .views import signup, user_profile, edit_profile

urlpatterns = [
    path("", views.home, name="home"),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('user/<int:user_id>/', user_profile, name='user_profile'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), # new
    path('edit-profile/', edit_profile, name='edit_profile'),
    # path('addpost/', addpost.as_view(), name='addpost')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)