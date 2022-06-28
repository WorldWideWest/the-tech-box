from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializer import ArticleSerializer
from .models import Article

@api_view(http_method_names = ["GET"])
def get_all(request):
    serializer = ArticleSerializer(
        Article.objects.all(), many = True)
    return Response(serializer.data)

@api_view(http_method_names = ["GET"])
def get_by_id(request, id):
    serializer = ArticleSerializer(
        Article.objects.get(id = id))
    return Response(serializer.data)

@api_view(http_method_names = ["GET"])
def get_by_title(request, title):
    serializer = ArticleSerializer(
        Article.objects.filter(title__icontains = title), many = True)
    return Response(serializer.data)

