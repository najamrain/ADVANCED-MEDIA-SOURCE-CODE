from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import myForm
from .forms import UserForm
from .models import student
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def home(request):
    if request.user.is_authenticated:
        return redirect("/display")
    else:
        user = User.objects.all()
        return render(request, "base.html", {"user": user})


def index(request):
    if request.method == "POST":
        form = myForm(request.POST)

        if form.is_valid():
            # name = form.cleaned_data['name'] #This line is extremly right
            name = request.POST['name']
            email = request.POST['email']

            if student.objects.filter(name=name).exists():
                messages.info(request, "Username  is already taken")
                return redirect("/")
            elif student.objects.filter(email=email).exists():
                messages.info(request, "Email is alreay taken")
                return redirect("/")
            else:
                form.save()
            return redirect("/display")

    else:
        form = myForm()
    return render(request, "index.html", {'form': form})
    # if request.method == "POST":
    #     form = myForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     return redirect("/display")

    # else:
    #     form = myForm()
    # return render(request, "base.html", {'form': form})


def addShow(request):
    if request.user.is_authenticated:

        if request.method == "POST":
            form = myForm(request.POST)

            if form.is_valid():
                # name = form.cleaned_data['name']
                # email = form.cleaned_data['email']
                # if student.objects.filter(name=name).exists():
                #     messages.info(request, "Name already taken")
                #     return redirect("/as")
                # elif student.objects.filter(email=email).exists():
                #     messages.info(request, "E-mail already taken")
                #     return redirect("/as")

                # else:
                    form.save()
                    messages.info(request, "ONE RECORD ADDED TO DATABASE")

                    return redirect("/display")

        else:
            form = myForm()
        return render(request, "index.html", {'form': form})
    else:
        messages.info(request, "You need to login first")
        return redirect("/signin")


def delete(request, id):
    get = student.objects.get(pk=id)
    let = get.delete()
    messages.info(request, "ONE RECORD DELETED")
    return redirect("/display", {"let": let})


def update(request, id):
    if request.method == "POST":
        get = student.objects.get(pk=id)
        form = myForm(request.POST, instance=get)
        if form.is_valid():
            form.save()
            print("update function working")
            messages.info(request, "ONE RECORD UPDATED")

        return redirect("/display")
    else:
        get = student.objects.get(pk=id)
        form = myForm(instance=get)
        return render(request, "update.html", {"form": form})


def search(request):
    if request.method == "POST":
        name = request.POST['name']
        # name_icontains more useful than this name_iexact
        get = student.objects.filter(name__icontains=name)
        # print(get)
        if get.exists():
            return render(request, "display.html", {"get": get})

        else:
            messages.info(request, "No Match Founf")
            return redirect("/display")


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:

            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken Already")
                return redirect("/signup")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Exists")
                return redirect("/signup")
            else:
                user = User.objects.create_user(
                    username=username, first_name=first_name, last_name=last_name, email=email, password=password1)
                user.save()
                messages.info(request, "User Created Successfully")
                return redirect("/signin")
        else:
                messages.info(request, "Password didnt match")
                return redirect("/signup")


    else:
        userForm1 = UserForm()
        user = User.objects.all()
        return render(request, "userForm.html", {"userForm1": userForm1, "user": user})


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user, username)
        if user is not None:
            print(user)
            login(request, user)
            # user = User.objects.all()
            get = student.objects.all()
            messages.info(request, "Successfully logedin")
            return redirect("/display")
        else:
            messages.error(request, "Invalid Username or Password")
            return redirect("/signin")
    else:
        # user = User.objects.all()
        return render(request, "signin.html")


def signout(request):
    logout(request)
    return redirect("/")


def display(request):
    if request.user.is_authenticated:
        get = student.objects.all()
        if len(get) <= 0:
            nnn = "Nothing To Show"
            return render(request, "display.html", {"nnn": nnn})
        else:
            user = User.objects.all()
            return render(request, "display.html", {"get": get})
    else:
        messages.error(request, "You need to login first")
        return redirect("/signin")
