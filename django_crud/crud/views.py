from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import PostInfo
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostInfoSerializer
import requests


# Create your views here.
class PostInfoClass(APIView):
    def get(self, request):
        posts = PostInfo.objects.all()
        serializer = PostInfoSerializer(posts, many=True)
        return Response(serializer.data)


def index(request):
    posts = {
        'posts': PostInfo.objects.all()
    }
    return render(request, 'crud/index.html', posts)


def index2(request):
    apiData= requests.get('http://localhost:8000/data').json()
    return render(request, 'crud/index2.html', {'apiData': apiData})


def createPage(request):
    return render(request, 'crud/create.html', {'title': 'Create'})


def create(request):
    question = request.POST["question"]
    answer = request.POST["answer"]
    isActive = request.POST["isActive"]

    post_info = PostInfo(question=question, answer=answer, isActive=isActive)
    post_info.save()
    return redirect('crud_index')


def editPage(request, id):
    post_by_id = {
        'post': PostInfo.objects.get(pk=id)
    }
    return render(request, 'crud/edit.html', post_by_id)


def update(request, id):
    post_info = PostInfo.objects.get(pk=id)
    post_info.question = request.POST["question"]
    post_info.answer = request.POST["answer"]
    post_info.isActive = request.POST["isActive"]
    post_info.save()

    return redirect('crud_index')


def delete(request, id):
    PostInfo.objects.filter(id=id).delete()

    return redirect('crud_index')

