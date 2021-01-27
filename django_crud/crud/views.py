from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import PostInfo

# Create your views here.


def index(request):
    posts = {
        'posts': PostInfo.objects.all()
    }

    return render(request, 'crud/index.html', posts)


def createPage(request):
    return render(request, 'crud/create.html', {'title': 'Create'})


def create(request):
    question = request.POST["question"]
    answer = request.POST["answer"]
    isActive = request.POST["isActive"]

    post_info = PostInfo(question=question, answer=answer, isActive=isActive)
    post_info.save()
    return redirect('crud_index')
