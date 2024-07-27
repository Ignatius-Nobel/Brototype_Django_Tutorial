from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

def signup(request):
    user = None
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
    return render(request, 'users/create.html',{'user':user})
