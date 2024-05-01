from django.contrib import admin


from .models import User

admin.site.register(User)

# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .models import CustomUser
#
#
# class CustomUserAdmin(BaseUserAdmin):
#     model = CustomUser
#     list_display = ('email', 'date_joined', 'last_online', 'is_staff', 'is_active')
#     list_filter = ('is_staff', 'is_superuser', 'is_active')
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal info', {'fields': ('date_of_birth', 'image')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
#         ('Important dates', {'fields': ('last_login', 'date_joined', 'last_online')}),
#         ('Additional info', {'fields': ('rating', 'posts')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser'),
#         }),
#         ('Personal info', {'fields': ('date_of_birth', 'image')}),
#         ('Additional info', {'fields': ('rating', 'posts')}),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)
#     filter_horizontal = ()
#
#
# admin.site.register(CustomUser, CustomUserAdmin)
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
#
# from .forms import CustomUserCreationForm, CustomUserChangeForm
# from .models import CustomUser
# from django.contrib.auth import get_user_model
# User = get_user_model()
#
# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ["email", "username",]
#
# admin.site.register(CustomUser, CustomUserAdmin)

