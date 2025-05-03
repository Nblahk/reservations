from django.contrib.auth.forms import UserCreationForm  
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect , render
from django.contrib import messages
from .forms.UserSignUpForm import UserSignUpForm
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm
from django.contrib.auth.models import User


from .forms.UserSignUpForm import UserSignUpForm
from .forms.UserUpdateForm import UserUpdateForm





class UserUpdateView(UserPassesTestMixin, UpdateView):
    model         = User
    form_class    = UserUpdateForm
    template_name = "users/update.html"
    success_url   = reverse_lazy("accounts:user-profile")

    def test_func(self):
        pk = self.kwargs.get('pk')
        return (
            self.request.user.is_authenticated
            and (self.request.user.id == pk or self.request.user.is_superuser)
        )

    def handle_no_permission(self):
        messages.error(self.request, "Vous n'avez pas l'autorisation d'accéder à cette page !")
        return redirect('accounts:user-profile')

class UserSignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class UserSignUpView(UserPassesTestMixin, CreateView):

    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def test_func(self):
        return self.request.user.is_anonymous or self.request.user.is_superuser
    
    def handle_no_permission(self):
        messages.error(self.request, "Vous êtes déjà inscrit!")
        return redirect('home')
@login_required
def profile(request):
    """
    Vue de la page de profil : affiche prénom, nom, email et langue choisie.
    Protégée par login_required.
    """
    # Dictionnaire pour traduire le code langue en label
    languages = {
        "fr": "Français",
        "en": "English",
        "nl": "Nederlands",
    }

    # Récupérer la langue stockée en one-to-one via UserMeta
    # Attention : adapte le nom de relation si tu as mis autre chose
    try:
        user_meta = request.user.usermeta
        lang_code = user_meta.langue
    except (AttributeError, request.user.DoesNotExist):
        lang_code = ""

    return render(request, 'users/profile.html', {
        'user_language': languages.get(lang_code, "—"),
    })
