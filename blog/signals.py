from django.contrib.auth.signals import user_logged_in, user_login_failed
from django.dispatch import receiver
from .models import LoginIntento

def get_ip(request):
    x_forwarded = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded:
        return x_forwarded.split(',')[0]
    return request.META.get('REMOTE_ADDR')

@receiver(user_logged_in)
def login_exitoso(sender, request, user, **kwargs):
    LoginIntento.objects.create(
        usuario=user.username,
        exitoso=True,
        ip=get_ip(request)
    )

@receiver(user_login_failed)
def login_fallido(sender, request, credentials, **kwargs):
    LoginIntento.objects.create(
        usuario=credentials.get('username', ''),
        exitoso=False,
        ip=get_ip(request)
    )