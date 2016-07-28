from django.shortcuts import render, redirect,HttpResponse
from ..users.models import User, UserManager
from .models import Wish

def index(request):
    user = User.objects.get(id=request.session['user'])
    mywishcreators = Wish.objects.filter(creator=user)
    mywish = Wish.objects.filter(otherusers=user).exclude(creator=user)
    allwishes = Wish.objects.exclude(otherusers = user)
    context = {
    'user':user.name,
    'mywishes':mywish,
    'allwishes':allwishes,
    'mywishcreators':mywishcreators

    }
    # print context
    return render(request, "wishes/index.html",context)
def additem(request):
    return render(request, "wishes/newitem.html")

def create(request):
    user = User.objects.get(id=request.session['user'])
    item = request.POST['item']
    error = Wish.wishManager.getErrors(item)
    if len(error) == 0:
        wish=Wish.objects.create(item = request.POST['item'],creator=user)
        wish.otherusers.add(user)
        return redirect("dashboard")
    else:
        context = {
            'logerrors':error
        }
        return render(request, "wishes/newitem.html", context)
def show(request,id):
    user = User.objects.get(id=request.session['user'])
    wish = Wish.objects.get(id=id)

    otherusers = Wish.objects.get(id=id).otherusers.exclude(id=wish.creator.id)
    creator = Wish.objects.get(id=id)
    print creator.creator.name
    # otherusers = otherusers.exclude(id=user.id)
    context={
    'wish':Wish.objects.get(id=id),
    'otherusers':otherusers,
    'creator':creator
    }
    return render(request, "wishes/show.html",context)
def addtolist(request, id):
    user = User.objects.get(id=request.session['user'])
    wish = Wish.objects.get(id=id)
    wish.otherusers.add(user)
    wish.save()
    print wish
    return redirect("dashboard")
def remove(request, id):
    user = User.objects.get(id=request.session['user'])
    wish = Wish.objects.get(id=id)
    wish.otherusers.clear()
    return redirect("dashboard")
def delete(request,id):
    wish = Wish.objects.get(id=id)
    wish.delete()
    return redirect("dashboard")
