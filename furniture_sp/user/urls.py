from django.urls import path, include
from .views import Login, Logout, Registrate, PasswordChange, PasswordReset, PasswordResetDone,\
    PasswordResetConfirm, PasswordResetComplete, profile

app_name = 'user'
urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('registrate/', Registrate.as_view(), name='registrate'),
    path('profile/', profile, name='profile'),
    path('password-change/', PasswordChange.as_view(), name='ps-change'),
    path('password-reset/', PasswordReset.as_view(), name='ps-reset'),
    path('password-reset-done/', PasswordResetDone.as_view(), name='ps-reset-done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='ps-reset-confirm'),
    path('password-reset-complete/', PasswordResetComplete.as_view(), name='ps-reset-complete')
]