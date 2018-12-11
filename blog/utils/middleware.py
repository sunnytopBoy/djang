from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from back.models import User


class LoginUserMiddleware(MiddlewareMixin):

    def process_request(self, request):

        if request.path in ['/back/login/', '/back/register/']:
            return None

        user_id = request.session.get('user_id')
        if user_id:
            user = User.objects.get(pk=user_id)
            request.user = user
            return None
        else:
            return HttpResponseRedirect(reverse('back:login'))

    def process_response(self, request, response):
        return response