from django.shortcuts import render
from .models import Blog
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import BlogSerializers
from rest_framework.views import APIView

class BlogListCreate(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers

    def delete(self, request):
        Blog.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BlogRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers
    lookup_field = "pk"

class BlogList(APIView):
    def get(self, request, format=None):
        title = request.query_params.get("title","")
        if title:
            blog = Blog.objects.filter(title__icontains=title)
        else:
            blog = Blog.objects.all()

        serializer = BlogSerializers(blog, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    