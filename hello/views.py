from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # クエリパラメータを渡されていなくてもエラーにならない処理
    if 'msg' in request.GET:
        msg = request.GET['msg']
        result = 'you typed: "' + msg + '".'
    else:
        result = 'please send msg parameter!'
    return HttpResponse(result)

def show(request, id, nickname):
    result = 'your id: ' + str(id) + ', name: "' \
        + nickname + '".'
    return HttpResponse(result)

def another_pattern(request, nickname, age):
    result = 'your account: ' + nickname + '" (' + str(age) + ').'
    return HttpResponse(result)
