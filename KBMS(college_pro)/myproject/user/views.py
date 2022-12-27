from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Article,question

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import MyForm,MyquestionForm


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method=='POST':
        firstname=request.POST.get('fname')
        lastname=request.POST.get('lname')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')

        register=False
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username is taken')
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email is taken')
                return redirect('/')
            else:
                user=User.objects.create_user(username=username,password=password1,first_name=firstname,last_name=lastname,email=email)
                user.save()
                register=True
                print("succesfully created")
                return render(request,'login.html')
        else:
            messages.info(request,'password not matching')
            return redirect('/')


    else:
        return render(request,'register.html')


def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            print("login succesfully")
            return redirect('/')
        else:
            messages.info(request,'Invalid username or password!')
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def ArticleList(request):
    if request.method == 'GET':
        query = request.GET.get('searchtext')

        submitbutton = request.GET.get('submit')

        if query is not None:


            results = Article.objects.all().filter(Q(title__iexact=query))



            context = {'results': results,
                        'submitbutton': submitbutton}

            return render(request,'articlelist.html',context)

        else:
            return render(request, 'articlelist.html')

    else:
            return render(request,'articlelist.html')


class AriticleView(DetailView):
    model=Article
    template_name = 'articleview.html'
    context_object_name = 'detail'


class ArticleCreate(CreateView):
    form_class = MyForm
    model = Article
    template_name = 'articlecreate.html'
    success_url = '/'


class dashboarddetail(ListView):
    model = Article
    template_name = 'dashbord.html'
    context_object_name = 'dashboard'

class Articleupdate(UpdateView):
    form_class = MyForm
    model = Article
    template_name = 'articlecreate.html'

class Articledelete(DeleteView):
    model = Article
    template_name = 'articledelete.html'
    success_url = '/'

class QuestionForm(CreateView):
    form_class = MyquestionForm
    model = question
    template_name = 'questionform.html'
    context_object_name = 'question_form'
    success_url = 'thankyou'

class QuestionList(ListView):
    model = question
    template_name = 'questionlist.html'
    context_object_name = 'userquestion'

def Thankyou(request):
    return render(request,'thankyou.html')

def service(request):
    return render(request,'service.html')
