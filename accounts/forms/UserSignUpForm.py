# accounts/forms/UserSignUpForm.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from catalogue.models import UserMeta

User = get_user_model()

class UserSignUpForm(UserCreationForm):
    class Language(forms.ChoiceField):
        choices = [
            ("", "Choisissez votre langue"),
            ("fr", "Français"),
            ("en", "English"),
            ("nl", "Nederlands"),
        ]

    first_name = forms.CharField(label='Prénom', max_length=60)
    last_name  = forms.CharField(label='Nom',     max_length=60)
    email      = forms.EmailField(label='E-mail')
    langue     = forms.ChoiceField(label='Langue', choices=Language.choices)

    class Meta:
        model  = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'langue',
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name  = self.cleaned_data['last_name']
        user.email      = self.cleaned_data['email']
        if commit:
            user.save()

            # ajouter au groupe MEMBER
            member = Group.objects.get(name='MEMBER')
            member.user_set.add(user)

            # créer le UserMeta
            langue = self.cleaned_data.get('langue')
            if langue:
                meta = UserMeta(user=user, langue=langue)
                meta.save()

        return user
