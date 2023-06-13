from django.http import HttpResponse
from django.shortcuts import render


def above(request):
    return HttpResponse('this is above home')


def my_home(request):
    return render(request, 'home.html', {'key_viese': 'hello world'})

def reverse(request):
    user_text = request.  GET['usertext']
    reversed_text = user_text[::-1]
    num_ = user_text.count(' ')
    return render(request, 'reverse.html',
                  {'usertext': user_text,
                   'reversedtext': reversed_text,
                   'num': num_})