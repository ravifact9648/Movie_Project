from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testapp.forms import SignUpForm
from django.http import HttpResponse
from testapp.forms import MovieForm
from testapp.models import Movie

# Create your views here.
def index(request):
    return render(request,"testapp/index.html")

@login_required
def addmovie(request):
    form=MovieForm()
    if request.method=='POST':
        form=MovieForm(request.POST)
        form.save()
    return render(request,'testapp/addmovie.html',{'forms':form})

def listmovie(request):
    movielist=Movie.objects.all()
    return render(request,'testapp/movielist.html',{'movielist':movielist})


def count_views(request):
    if 'count' in request.COOKIES:
        newcount=int(request.COOKIES['count'])+1
    else:
        newcount=1
    response=render(request,'testapp/count.html',{'count':newcount})
    response.set_cookie('count',newcount)
    return response


def signup(request):
    form=SignUpForm()
    if request.method=='POST':
        print("validating")
        form=SignUpForm(request.POST)
        if form.is_valid():
          form.save()
    return render(request,'testapp/signup.html',{'form':form})


