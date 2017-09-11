from django.contrib.auth.models import User
from core.models import Artist
from django import forms
from settings import form_default_errors
from django.contrib.auth import update_session_auth_hash


# Форма для изменения профиля пользователя
class UpdateProfileForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        help_text='Пожалуйста укажите валидный email',
        widget=forms.EmailInput(attrs={'class': 'forms_input'}),
        error_messages=form_default_errors)
    username = forms.RegexField(
        required=True,
        help_text='Псевдоним должен быть уникальным. Ссылка на ваше портфолио будет выглядеть http://artifex.ru/псевдоним',
        label='Псевдоним',
        widget=forms.TextInput(attrs={'class': 'forms_input'}),
        max_length=30,
        regex=r'^[\w-]+$',
        error_messages=form_default_errors)
    first_name = forms.RegexField(
        required=False,
        help_text='Пожалуйста укажите ваше настоящее имя',
        label='Имя',
        widget=forms.TextInput(attrs={'class': 'forms_input'}),
        max_length=30,
        regex=r'^[\w-]+$',
        error_messages=form_default_errors)
    last_name = forms.RegexField(
        required=False,
        help_text='Пожалуйста укажите вашу настоящую фамилию',
        label='Фамилия',
        widget=forms.TextInput(attrs={'class': 'forms_input'}),
        max_length=30,
        regex=r'^[\w-]+$',
        error_messages=form_default_errors)
    site_url = forms.URLField(
        required=False,
        help_text='Укажите здесь ваш персональный сайт, если он у вас есть',
        label='Сайт',
        initial="http://",
        widget=forms.URLInput(attrs={'class': 'forms_input'}),
        error_messages=form_default_errors)
    twitter_name = forms.RegexField(
        required=False,
        help_text='Укажите ваш ник в Twitter, чтобы другие могли найти вас там',
        label='Twitter',
        widget=forms.TextInput(attrs={'class': 'forms_input'}),
        max_length=15,
        regex=r'^[\w-]+$',
        error_messages=form_default_errors)

    class Meta:
        model = Artist
        fields = ('first_name', 'last_name', 'email', 'username', 'site_url', 'twitter_name')

    def clean_username(self):
        username = self.cleaned_data['username']

        # старое значение совпадает с новым, ничего не поменялось
        if self.instance and (self.instance.username == username):
            return username

        user = User.objects.filter(username=username)
        if user:
            raise forms.ValidationError('Такой псевдоним уже зарегистрирован.')

        return username

    def clean_email(self):
        email = self.cleaned_data['email']

        # старое значение совпадает с новым, ничего не поменялось
        if self.instance and (self.instance.email == email):
            return email

        user = User.objects.filter(email=email)
        if user:
            raise forms.ValidationError('Пользователь с таким email уже зарегистрирован.')

        return email


# Форма для изменения информации пользователя "о себе"
class UpdateAboutForm(forms.ModelForm):
    information = forms.CharField(
        required=True,
        label='О себе',
        widget=forms.Textarea(attrs={'class': 'about_textarea'}),
        error_messages=form_default_errors
    )

    class Meta:
        model = Artist
        fields = ('information',)


 # Форма для изменения профиля пользователя
class ChangePasswordForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

    old_password = forms.CharField(
        required=True,
        help_text='Введите старый пароль',
        label='Старый пароль',
        widget=forms.PasswordInput(attrs={'class': 'forms_input'}),
        error_messages=form_default_errors)
    new_password = forms.CharField(
        required=True,
        help_text='Введите новый пароль. Пароль не должен быть меньше 6 символов',
        label='Новый пароль',
        widget=forms.PasswordInput(attrs={'class': 'forms_input'}),
        error_messages=form_default_errors)

    class Meta:
        model = Artist
        fields = ('old_password', 'new_password')

    def clean_old_password(self):
        old_password = self.cleaned_data['old_password']

        if not self.instance.request.user.check_password(old_password):
            raise forms.ValidationError('Старый пароль введен неверно')
        return old_password

    def clean_new_password(self):
        new_password = self.cleaned_data['new_password']

        if len(new_password) < 6:
                raise forms.ValidationError('Новый пароль слишком короткий')
        return new_password

    def save(self, commit=True):
        new_password = self.cleaned_data['new_password']
        self.instance.request.user.set_password(new_password)
        self.instance.request.user.save()

        update_session_auth_hash(self.instance.request, self.instance.request.user)

        return self.instance.request.user



