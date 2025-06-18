from django.urls import path
from . import views

app_name = 'user_account'

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('password_change/', views.UserPasswordChangeView.as_view(), name='password_change'),
]