from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User

# Create your views here.

def index(request):
    return HttpResponse('<em>Hello World<em>')

#
# def help(request):
#     my_dict = {'help_text': 'Pleaes read if you need help'}
#     return render (request, 'AppTwo/index.html', context=my_dict)

def user(request):
    user_list  = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render (request, 'AppTwo/users.html', context= user_dict)
