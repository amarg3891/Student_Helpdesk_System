from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm, LoginForm
from django.contrib import messages # for print the message
from django.contrib.auth import authenticate, login ,logout
from .models import StudentCourse,StudentSyllabus


# Create your views here.
def home(request):
    stu = StudentCourse.objects.all()
    return render(request,'home.html', {'stu':stu})

def course(request,pk):
    # stu = StudentCourse.objects.all()
    stud = StudentCourse.objects.get(pk=pk)
    return render(request, 'bca.html', {'stud':stud})

# Here User(Author) will register for login by passing some of the Required Fields.
def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'Successfully!! Registered')
            user = form.save()
            return HttpResponseRedirect('login')
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form':form})

# After Signup, By Unique username and password you will be logged into Blog.
def log_in(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged In Successfully !!')
                    return HttpResponseRedirect('/')
        else:
            form = LoginForm()
        return render(request, 'login.html' ,{'form':form})
    else:
        return HttpResponseRedirect('/')


# Logout function will auto redirect to you on Portfolio.
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def syllabus(request):
    syl = StudentSyllabus.objects.all()
    return render(request, 'syllabus.html', {'syl':syl})
