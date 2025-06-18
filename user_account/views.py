from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserAccountCreationForm, UserLoginForm

# Create your views here.
class UserRegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserAccountCreationForm
    success_url = reverse_lazy('tasks:task_create')

    def form_valid(self, form):
        response = super().form_valid(form)
        # Optionally, you can add logic here after successful registration
        return response
class UserLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = UserLoginForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        response = super().form_valid(form)
        # Optionally, you can add logic here after successful login
        return response
class UserLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'logout.html'
    next_page = reverse_lazy('user_account:logout')

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        # Optionally, you can add logic here after successful logout
        return response
        
class UserProfileView(LoginRequiredMixin, FormView):
    template_name = 'profile.html'
    form_class = UserLoginForm  # You can use a different form for profile editing
    success_url = reverse_lazy('user_account:profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

    def form_valid(self, form):
        # Handle profile update logic here if needed
        return super().form_valid(form)

class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView): 
    template_name = 'password_change.html'
    form_class = PasswordChangeForm # Use a form for password change
    success_url = reverse_lazy('user_account:profile')

    def form_valid(self, form):
        # Handle password change logic here if needed
        return super().form_valid(form)
