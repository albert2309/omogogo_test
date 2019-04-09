from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import BucketlistSerializer, TagSerializer, MemberSerializer ,PostActivitySerializer, TodoSerializer
from .models import Bucketlist, Tag, Member, PostActivity, Todo


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

class CreateTagView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def perform_create(self, serializer):
        serializer.save()

class DetailTagView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class CreateMemberView(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def perform_create(self, serializer):
        serializer.save()

class DetailMemberView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class CreatePostActivityView(generics.ListCreateAPIView):
    queryset = PostActivity.objects.all()
    serializer_class = PostActivitySerializer

    def perform_create(self, serializer):
        serializer.save()

class DetailPostActivityView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostActivity.objects.all()
    serializer_class = PostActivity

class CreatePostActivityView(generics.ListCreateAPIView):
    queryset = PostActivity.objects.all()
    serializer_class = PostActivitySerializer

    def perform_create(self, serializer):
        serializer.save()

class DetailPostActivityView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostActivity.objects.all()
    serializer_class = PostActivity

class CreateTodoView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        serializer.save()

class DetailTodoView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer