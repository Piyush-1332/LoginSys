from django.contrib.auth.views import (
                    LoginView,
                    LogoutView,
                    PasswordResetView,
                    PasswordResetDoneView,
                    PasswordResetConfirmView,
                    PasswordResetCompleteView)
from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('login',LoginView.as_view(template_name='folder/login.html'),name="login"),
    path('logout',LogoutView.as_view(template_name='folder/logout.html'),name="logout"),
    path('register',views.register,name='register'),
    path('profile',views.profile,name="profile"),
    path('profile/edit',views.profile_edit, name="edit"),

]
