import json
from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login
from django.views import generic, View
from app.models import User, Issue

# Create your views here.

dummy = {
            'data': 'welcome to SIT v2 @python',
            'meta': {
                    'status_code': 200,
                },
        }


def home(request):
    return JsonResponse(dummy)


class IssueView(View):

    def get(self, request):
        """
        get all the issues
        """
        return HttpResponse('get issue')
    
    def post(self, request):
        """
        create issue
        """
        if request.content_type == 'application/json':
            body_unicode = request.body.decode('utf-8')
            issue_req = json.loads(body_unicode)
            issue = Issue()
            issue.title = issue_req["title"]
            issue.description = issue_req["description"]
            issue.author = request.user
            issue.assignee_id = issue_req["assignee_id"]
            issue.status = issue_req["status"]
            issue.save()

            return HttpResponse(serialize_object(issue), content_type='application/json')

        return HttpResponse('post issue')

class IssueDetailsView(View):

    def get(self, request, **kwargs):
        issue_id = self.kwargs['issue_id']
        return HttpResponse('get issue, %d'.format(issue_id))
    
    def patch(self, request, issue_id):
        issue_id = self.kwargs['issue_id']
        return HttpResponse('patch issue, %d'.format(issue_id))

    def delete(self, request, issue_id):
        issue_id = self.kwargs['issue_id']
        return HttpResponse('delete issue, %d'.format(issue_id))


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


def serialize_object(issue):
    data = serializers.serialize('json', [issue])
    struct = json.loads(data)
    return json.dumps(struct[0])