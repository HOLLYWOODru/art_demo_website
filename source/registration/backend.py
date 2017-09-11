from django.contrib.auth import get_user_model
from core.models import Artist

class EmailOrUsernameModelBackend(object):
    def authenticate(self, username=None, password=None):

        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}

        try:
            artifexUser = Artist.objects.get(**kwargs)

            if artifexUser.check_password(password):
                return artifexUser
        except Artist.DoesNotExist:
            userModel = get_user_model()

            try:
                user = userModel.objects.get(**kwargs)
                if user.check_password(password):
                    return user
            except userModel.DoesNotExist:
                return None

    def get_user(self, user_id):

        try:
            return Artist.objects.get(pk=user_id)
        except Artist.DoesNotExist:
            userModel = get_user_model()

            try:
                return userModel.objects.get(pk=user_id)
            except userModel.DoesNotExist:
                return None