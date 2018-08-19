from datetime import datetime
from django.http import HttpResponse


from app.models import User

class LoginRequiredMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        if view_func.__name__ != "post_login":
            try:
                token = request.META['HTTP_AUTHORIZATION']
            except (KeyError):
                return HttpResponse('401 Unauthorized', status=401)

            try:
                user = User.objects.get(access_token=token)
            except (KeyError, User.DoesNotExist):
                return HttpResponse('401 Unauthorized', status=401)
            request.user = user

    
    