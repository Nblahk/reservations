from django.urls import path
from .views import UserSignUpView, profile
from django.views.generic.base import RedirectView 

app_name = 'accounts'

urlpatterns = [
    path('',        RedirectView.as_view(pattern_name='login', permanent=False), name='account-root'),
    path('signup/', UserSignUpView.as_view(), name='user-signup'),
    path('profile/', profile, name='user-profile'),
]

