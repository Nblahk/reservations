from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from catalogue.models import UserMeta

User = get_user_model()

class UserUpdateForm(UserChangeForm):
    # on masque le champ mot de passe
    password = None

    # choix de langues
    LANG_CHOICES = [
        ("",   "Choisissez votre langue"),
        ("fr", "Français"),
        ("en", "English"),
        ("nl", "Nederlands"),
    ]
    langue = forms.ChoiceField(choices=LANG_CHOICES, label="Langue")

    class Meta:
        model  = User
        fields = ['username', 'first_name', 'last_name', 'email', 'langue']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # personnalisations des labels
        self.fields['username'].label   = "Login"
        self.fields['first_name'].label = "Prénom"
        self.fields['last_name'].label  = "Nom"
        self.fields['email'].label      = "E-mail"

        # initialisation de la langue depuis UserMeta
        user = kwargs.get('instance')
        if user and hasattr(user, 'usermeta'):
            self.initial['langue'] = user.usermeta.langue

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # update ou création de UserMeta
            meta, _ = UserMeta.objects.get_or_create(user=user)
            meta.langue = self.cleaned_data['langue']
            meta.save()
        return user
