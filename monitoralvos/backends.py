from django.contrib.auth.backends import ModelBackend
from login_sca import login
from django.contrib.auth.models import User

authorization = 'http://apps.mprj.mp.br/mpmapas/api/authentication'
authentication = 'http://apps.mprj.mp.br/mpmapas/api/authenticate'

class MprjBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        password = bytes(password, 'utf-8')
        resp = login(username, password, authorization, authentication)
        if resp.auth.status_code == 200:
            return User.objects.get(username=username)
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
