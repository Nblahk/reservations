from django.urls import path
from django.views.generic.base import RedirectView 
from .views import UserSignUpView, UserUpdateView, profile, delete

app_name = 'accounts'

urlpatterns = [
    path('',        RedirectView.as_view(pattern_name='login', permanent=False), name='account-root'),
    path('signup/', UserSignUpView.as_view(), name='user-signup'),
    path('profile/', profile, name='user-profile'),
    path('profile/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    path('profile/delete/<int:pk>/', delete,               name='user-delete'),
]

