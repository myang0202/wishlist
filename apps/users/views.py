from django.shortcuts import render, redirect,HttpResponse
from .models import User, UserManager

def index(request):
    return render(request, "users/index.html")
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    error = User.userManager.loginValidation(username, password)
    if len(error)==0:
        print "good"
        user = User.objects.get(username=username)
        request.session['user']=user.id
        return redirect("dashboard")

    else:
     context={
     'logerrors':error
     }
    return render(request, "users/index.html", context)
def register(request):
    name = request.POST['name']
    username = request.POST['username']
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']
    date = request.POST['date']
    error = User.userManager.getErrors(name,username, password,confirm_password, date)
    if len(error) == 0:
        encryptedPassword= User.userManager.encrypt(password)
        user = User.objects.create(name = name, username=username,password = encryptedPassword,date=date)
        return redirect("login_page")
    else:
        context = {
            'logerrors':error
        }
        return render(request, "users/index.html", context)
def logout(request):
    request.session.clear()
    return redirect("login_page")
# else:
#     username = request.POST['username']
#     password = request.POST['password']
