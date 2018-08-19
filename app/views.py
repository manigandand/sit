from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login

# Create your views here.

dummy = {
            'data': 'welcome to SIT v2 @python',
            'meta': {
                    'status_code': 200,
                },
        }


def home(request):
    return JsonResponse(dummy)


def post_login(request):
    username = request.POST['username']
    password = request.POST['password']
    print(username)
    print(password)

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        return JsonResponse(dummy)
    return JsonResponse({})


def issue(request):
    return JsonResponse(dummy)

