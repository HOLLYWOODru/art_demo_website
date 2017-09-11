from django import forms
from django.contrib.auth.models import User
from core.models import Artist
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from settings import form_default_errors


# Форма для регистрации
class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields.pop('password2')

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'forms_input'}),
        error_messages=form_default_errors)
    username = forms.RegexField(
        required=True,
        label='Псевдоним',
        widget=forms.TextInput(attrs={'class': 'forms_input'}),
        max_length=30,
        regex=r'^[\w-]+$',
        error_messages=form_default_errors)
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'forms_input'}),
        error_messages=form_default_errors)

    class Meta:
        model = Artist
        fields = ('username', 'email', 'password1')

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username)
        if user:
            raise forms.ValidationError('Такой псевдоним уже зарегистрирован.')
        return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        user = User.objects.filter(email=email)
        if user:
            raise forms.ValidationError('Пользователь с таким email уже зарегистрирован.')
        return email

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 6:
            raise forms.ValidationError('Пароль слишком короткий')
        return password

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            # not active until he opens activation link
            user.is_activated = False
            user.save()
        return user


# Форма авторизации
class UsernameAndEmailAuthenticationForm(AuthenticationForm):
    username = forms.RegexField(
        required=True,
        label='Псевдоним',
        widget=forms.TextInput(attrs={'class': 'forms_input'}),
        max_length=30,
        regex=r'^[\w-]+$',
        error_messages=form_default_errors)
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'forms_input'}),
        error_messages=form_default_errors)

    def clean_password(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).first()

        if not user:
            raise forms.ValidationError('Неверный логин или пароль')

        password = self.cleaned_data['password']

        if not user.check_password(password):
            raise forms.ValidationError('Неверный логин или пароль')

        return password