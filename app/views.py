import json
from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login

from app.models import User

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

    user = User.objects.get(email=username, password=password)
    if user is not None:
        print("here")
        data = serializers.serialize('json', [user])
        struct = json.loads(data)
        data = json.dumps(struct[0])
        
        return HttpResponse(data, content_type='application/json')
        # return JsonResponse({"data": data}, safe=True)
    else:
        return JsonResponse(dummy)
    return JsonResponse({})


def issue(request):
    return JsonResponse(dummy)

