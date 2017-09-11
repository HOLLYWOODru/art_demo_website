from django.views.generic import UpdateView
from core.models import Artist
from django.http import Http404, HttpResponse
from .forms import UpdateProfileForm, UpdateAboutForm, ChangePasswordForm
from django.core.urlresolvers import reverse


# Abstract Artist Update View
class ArtistUpdateView(UpdateView):
    model = Artist

    def get(self, request, *args, **kwargs):
        try:
            artist = self.get_object()
        except Exception as e:
            return HttpResponse('Доступ в личный кабинет возможен только художникам')

        self.object = artist
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)

        return self.render_to_response(context)

    def get_object(self):
        artist = self.request.user

        if artist is None:
            raise Http404
        if not isinstance(artist, Artist):
            raise Http404

        return artist


# View for updating profile information
class ArtistProfileView(ArtistUpdateView):
    template_name = "user/profile.html"
    form_class = UpdateProfileForm

    def get_success_url(self):
        self.request.COOKIES['show_message'] = True
        return reverse('user.account.profile')

# View for updating profile information
class ArtistAboutView(ArtistUpdateView):
    template_name = "user/about.html"
    form_class = UpdateAboutForm

    def get_success_url(self):
        return reverse('user.account.about')


# View for changing password
class ArtistPasswordView(ArtistUpdateView):
    template_name = "user/password.html"
    form_class = ChangePasswordForm

    def get_success_url(self):
        return reverse('user.account.profile')

    def get_form(self, form_class):
        form = super(ArtistPasswordView, self).get_form(form_class)
        form.instance.request = self.request
        return form
