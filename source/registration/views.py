import hashlib
from django.contrib.auth.tokens import default_token_generator
import random

from django.contrib.auth import login, logout
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from registration.forms import RegistrationForm, UsernameAndEmailAuthenticationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from registration.models import UserProfile
from core.models import Artist
from django.template import RequestContext
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import authenticate, login



# Регистрация
def register_user(request):

    args = {}
    args.update(csrf(request))

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        args['form'] = form

        if form.is_valid():
            # save user to database if form is valid
            form.save()

            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']

            #Get artist by username
            artist = Artist.objects.get(username=username)

            activation_key = default_token_generator.make_token(artist)

            # Create and save user profile
            new_profile = UserProfile(user=artist, activation_key=activation_key)
            new_profile.save()

            # Send email with activation key
            email_subject = 'Активация аккаунта'
            email_body = "Приветствуем %s! Спасибо за регистрацию на нашем сайте. Чтобы активировать ваш аккаунт,  \
            перейдите по ссылке: http://127.0.0.1:8000/confirm/%s" % (username, activation_key)

            #print('email body:')
            #print(email_body)

            #send_mail(email_subject, email_body, settings.DEFAULT_FROM_EMAIL, [email], fail_silently=False)

            new_user = authenticate(username=username,
                                    password=password)
            login(request, new_user)

            return HttpResponseRedirect('/')
    else:
        args['form'] = RegistrationForm()
    return render_to_response('registration/register.html', args, context_instance=RequestContext(request))


# Логин
def log_in_user(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')

    args = {}
    args.update(csrf(request))

    if request.method == 'POST':
        form = UsernameAndEmailAuthenticationForm(request, data=request.POST)
        args['form'] = form

        if form.is_valid():
            user = form.get_user()

            if user is not None:
                login(request, form.get_user())

                redirect_url = request.POST.get('next', None)

                if redirect_url is None:
                    redirect_url = '/'

                return HttpResponseRedirect(redirect_url)
            else:

                return render_to_response('registration/login.html', args, context_instance=RequestContext(request))
        else:

            return render_to_response('registration/login.html', args, context_instance=RequestContext(request))
    else:
        redirect_url = request.GET.get('next', None)

        if redirect_url is None:
            redirect_url = '/'

        args['form'] = UsernameAndEmailAuthenticationForm()
        args['next'] = redirect_url

    return render_to_response('registration/login.html', args, context_instance=RequestContext(request))

# Log out
def log_out_user(request):
    logout(request)

    return HttpResponseRedirect('/')


# Подтверждение регистрации
def register_confirm(request, activation_key):

    #check if user is already logged in and if he is redirect him to some other url, e.g. home
    if request.user.is_authenticated():
        HttpResponseRedirect('/')

    # check if there is UserProfile which matches the activation key (if not then display 404)
    user_profile = get_object_or_404(UserProfile, activation_key=activation_key)

    #check if the activation key has expired, if it hase then render confirm_expired.html
    if user_profile.key_expires < timezone.now():
        return render_to_response('registration/confirm_expired.html')

    #if the key hasn't expired save user and set him as active and render some template to confirm activation
    user = user_profile.user
    user.is_activated = True
    user.save()

    return render_to_response('registration/confirm.html')