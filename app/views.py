import json
from django.shortcuts import render, get_object_or_404
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
        issue_list = Issue.objects.order_by('-created_at')
        return HttpResponse(serialize_object(issue_list, False), content_type='application/json')
        
    
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

            return HttpResponse(serialize_object(issue, True), content_type='application/json')

        return HttpResponse('post issue')

class IssueDetailsView(View):

    def get(self, request, **kwargs):
        issue_id = self.kwargs['issue_id']
        # issue = get_object_or_404(Issue, pk=issue_id)

        try:
           issue = Issue.objects.get(pk=issue_id)
        except (KeyError, Issue.DoesNotExist):
            return HttpResponse('404 Issue Not found', status=404)

        return HttpResponse(serialize_object(issue, True), content_type='application/json')

    
    def patch(self, request, issue_id):
        issue_id = self.kwargs['issue_id']
        return HttpResponse('patch issue, %d'.format(issue_id))

    def delete(self, request, issue_id):
        issue_id = self.kwargs['issue_id']
        try:
           issue = Issue.objects.get(pk=issue_id)
        except (KeyError, Issue.DoesNotExist):
            return HttpResponse('404 Issue Not found', status=404)
        # delete
        issue.delete()

        return HttpResponse('204 No Content', status=204)

def post_login(request):
    username = request.POST['username']
    password = request.POST['password']

    user = User.objects.get(email=username, password=password)
    if user is not None:
        return HttpResponse(serialize_object(user, True), content_type='application/json')
    else:
        return JsonResponse(dummy)
    return JsonResponse({})


def serialize_object(obj, is_first_obj):
    if is_first_obj:
        data = serializers.serialize('json', [obj])
        struct = json.loads(data)
        data = json.dumps(struct[0])
    else:
        data = serializers.serialize('json', obj)
        struct = json.loads(data)
        data = json.dumps(struct)

    return data