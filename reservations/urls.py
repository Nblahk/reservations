"""reservations URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView



urlpatterns = [
    # Page d'accueil
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    # Comptes : inscription, profil, login/logout, password change
    path('accounts/', include('accounts.urls')),                # signup, profile
    path('accounts/', include('django.contrib.auth.urls')),     # login, logout, password_change, etc.

    # Catalogue
    path('catalogue/', include('catalogue.urls')),

    # Réinitialisation de mot de passe (admin)
    path(
        'admin/password_reset/',
        auth_views.PasswordResetView.as_view(
            extra_context={"site_header": admin.site.site_header}
        ),
        name="admin_password_reset"
    ),
    path(
        'admin/password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            extra_context={"site_header": admin.site.site_header}
        ),
        name="password_reset_done"
    ),
    path(
        'admin/reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            extra_context={"site_header": admin.site.site_header}
        ),
        name="password_reset_confirm"
    ),
    path(
        'admin/reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            extra_context={"site_header": admin.site.site_header}
        ),
        name="password_reset_complete"
    ),

    path('admin/', admin.site.urls),

]

# Personnalisation de l’interface d’administration
admin.site.index_title  = "Projet Réservations"
admin.site.index_header = "Projet Réservations HEADER"
admin.site.site_title   = "Spectacles"
