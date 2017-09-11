from django.conf import settings

def site_architecture(request):

    return {
        'site_architecture' : settings.SITE_ARCHITECTURE
    }