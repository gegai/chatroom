from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from blog import models
import json
from django.core.serializers.json import DjangoJSONEncoder
import datetime


class CJsonEncoder(json.JSONEncoder):
    def default(self,obj):
        if isinstance(obj,datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj,datetime.date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self,obj)


# Create your views here.
def index(request):
    return render(request, 'index.html')


def log(request):
    return render(request, 'log.html')


def submitchat(request):
    data1 = {'status': 0, 'author': '', 'create_time': ''}
    comment = request.POST.get('data')
    author_id = request.session['userprofile_id']
    current_comment = models.Comment.objects.create(comment=comment,
                                                    author_id=author_id)

    # user = models.UserProfile.objects.get(id=author_id)
    user = models.UserProfile.objects.get(id=author_id).name
    data1['id'] = current_comment.id
    data1['status'] = 1
    data1['author'] = user
    data1['create_time'] = current_comment.add_time.strftime('%Y-%m-%d %H:%M:%S')
    return HttpResponse(json.dumps(data1))


def register(request):
    username = request.POST.get('user')
    password = request.POST.get('passwd')
    models.UserProfile.objects.create(name=username,
                                      password=password)
    return HttpResponseRedirect('/log/')


def acc_login(request):
    name = request.POST.get('username')
    m = models.UserProfile.objects.get(name=name)
    if m.password == request.POST.get('pwd'):
        request.session['userprofile_id'] = m.id
        username = m.name
        request.session['username'] = username
        log = 1
        return render(request, 'index.html', {'username': username, 'log': log})
    else:
        return HttpResponse("Your username and password didn't match.")


def acc_logout(request):
    del request.session['username']
    log = 0
    return HttpResponseRedirect('/')


def getchat(request):
    chat = models.Comment.objects.all().order_by('-id')[0:20].values('id','comment','author__name','add_time')
    chat = list(chat)
    chat = json.dumps(chat,cls=CJsonEncoder)
    return HttpResponse(chat)


def getchat2(request):
    last_id = request.POST.get('lastid')
    chat = models.Comment.objects.filter(id__gt=last_id).values('id','comment','author__name','add_time')
    chat = list(chat)
    chat = json.dumps(chat, cls=CJsonEncoder)
    return HttpResponse(chat)