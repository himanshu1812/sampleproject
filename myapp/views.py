from django.shortcuts import render, HttpResponse, redirect
from .forms import StudentForm, UserForm
from .models import Student
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

#@method_decorator(login_required, name="dispatch")
class Sample(TemplateView):
    template_name = "index.html"
'''
def addstudent(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Data Inserted</h1>")
    else:
        form = StudentForm()
    return render(request, 'add.html', {'form': form})
'''

class addstudent(CreateView):
    form_class = StudentForm
    template_name = "add.html"

'''
def showstudent(request):
    data = Student.objects.all()
    return render(request, 'show.html', {"data": data})

'''

class showstudent(ListView):
    model = Student
    template_name = "show.html"

class deletestudent(DeleteView):
    model = Student
    template_name = "delete.html"
    success_url = "/show"
    
'''
def deletestudent(request, id):
    data = Student.objects.get(id=id)
    data.delete()
    return redirect("/show")
'''    
'''
def updatestudent(request, id):
	data = Student.objects.get(id=id)
	form = StudentForm(request.POST, instance=data)
	if form.is_valid():
		form.save()
		return redirect("/show")
	return render(request, 'edit.html', {"data":data})
'''
class updatestudent(UpdateView):
    model = Student
    form_class = StudentForm
    template_name  = "add.html"

def registration(request):
    if request.method=="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            e = form.cleaned_data['email']
            p = form.cleaned_data['password']
            User.objects.create_user(username=u,
                                        email=e,
                                        password=p)
            subject = "Demo Message"
            msg = "Thank YOu For Register"
            send_mail(subject,msg,settings.EMAIL_HOST_USER,[e])
            return HttpResponse("Registration Success")
    else:
        form = UserForm()
    return render(request, 'registration.html', {"form":form})

def loginpage(request):
    return render(request, 'login.html')    

def authuser(request):
    u = request.POST['username']    
    p = request.POST['password']
    user = authenticate(username=u, password=p)
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return HttpResponse("<h1>Login Failed</h1>")    

def logoutuser(request):
    logout(request)
    return redirect('/loginuser')
'''    
@login_required(login_url="/loginuser/")
def index(request):
    return render(request, 'index.html')
'''

