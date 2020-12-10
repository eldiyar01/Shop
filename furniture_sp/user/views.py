from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import RegistrateForm
from .models import User


def profile(request):
    return render(request, 'user/profile.html')


class Login(LoginView):
    template_name = 'user/login.html'


class Logout(LogoutView):
    template_name = 'user/login.html'


class Registrate(CreateView):
    template_name = 'user/register.html'
    form_class = RegistrateForm
    success_url = reverse_lazy('user:login')

    def get_queryset(self):
        return User.objects.all()


class PasswordChange(PasswordChangeView):
    template_name = 'user/password/change.html'
    success_url = reverse_lazy('user:profile')


class PasswordReset(PasswordResetView):
    template_name = 'user/password/reset.html'
    email_template_name = 'user/password/reset_email.html'
    success_url = reverse_lazy('user:ps-reset-done')


class PasswordResetDone(PasswordResetDoneView):
    template_name = 'user/password/reset_done.html'


class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = 'user/password/reset_confirm.html'
    success_url = reverse_lazy('user:ps-reset-complete')


class PasswordResetComplete(PasswordResetCompleteView):
    template_name = 'user/password/reset_complete.html'
