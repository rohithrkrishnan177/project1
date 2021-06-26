from pyexpat.errors import messages
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import logout
# Create your views here.
from .forms import loginform, registerform
from .models import userdb


def index(request):
    if 'username' in request.session.keys():
        name = request.session['username']
        n = request.session['name']
        print(n)
        print(name)
        context = {'message': 'hello!!!'}
        print("hai")
        print(context)
        return render(request, 'index.html', context)

def login(request):
    login_var = loginform()
    content = {'form': login_var}
    print("hai")
    if request.method == 'POST':
        print(request.method)
        login_var = loginform(request.POST)
        if login_var.is_valid():
            login_var.save()
            # msg = "<html><body>registered</body><html>"
            # return HttpResponse(msg)
            return HttpResponseRedirect('index')
        else:
            login_var = loginform()
    return render(request, 'login.html',content)


def logout(request):
    return redirect("login")

def reg(request):
    print("hello newuser")
    newuser_var = registerform()
    context = {'form': newuser_var}
    print("hello")
    if request.method == 'POST':
        print(request.method)
        newuser_var = registerform(request.POST)
        image = request.FILES['image']
        if newuser_var.is_valid():
            newuser_var.save()
            msg = "Sucessfully registered..."
            return render(request, 'reg.html',{'msg':msg})
        else:
            login_var = loginform()
    return render(request, "reg.html",context)


def viewlist(request):
    data = userdb.objects.all()
    print(data)
    datas1 = reversed(userdb.objects.all())

    datas=userdb.objects.order_by('id').reverse()
    print(datas)
    return render(request, 'viewlist.html',{'datas': datas})

def edituser(request,dataid):
    name=request.POST.get('name')
    email=request.POST.get('email')
    username=request.POST.get('username')
    password=request.POST.get('password')
    place=request.POST.get('place')
    userdb.objects.filter(id=dataid).update(name=name,email=email,username=username,password=password,place=place)
    return redirect('viewlist')

def profileupdate(request,dataid):
    data = userdb.objects.filter(id=dataid)
    return render(request, "profileupdate.html", {'data':data})


def deleteuser(request,dataid):
    userdb.objects.filter(id=dataid).delete()
    return redirect('viewlist')


def userlogin(request):
    if request.method == 'POST':
        print("hello")
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        print(password)

        if userdb.objects.filter(username=username,password=password).exists():
            data = userdb.objects.filter(username=username,password=password).values('name','email','id').first()
            print(data)
            request.session['id'] = data['id']
            request.session['name'] = data['name']
            request.session['username'] = username
            request.session['password'] = password
            request.session['email'] = data['email']
            return redirect('index')
        else:
            msg = "Invalid Username or password..."
            return render(request, 'login.html', {'msg':msg})
    else:
        return redirect('login')