from django.shortcuts import render
from login.forms import NewUserForm

def login_user(request):
    return render(request, 'login/index_login.html')

def user(request):
    login =  NewUserForm()
    #POST jesli forma została zatwierdzona
    if request.method == 'POST':
        login = NewUserForm(request.POST)

        if login.is_valid():
            login.save(commit=True)
            return login_user(request)
        else:
            print('Error form invalid')

    return render(request, 'login/login.html', {'login' : login})
# Create your views here.
