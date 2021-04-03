from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from news.models import Category, News
from .serializers import NewsSerializer, CategorySerializer


class NewsApiView(ListAPIView):
    serializer_class = NewsSerializer
    queryset = serializer_class.Meta.model.objects.filter(is_published=True)
    permission_classes = [AllowAny]


class SingleNewsApiView(RetrieveAPIView):
    serializer_class = NewsSerializer
    queryset = serializer_class.Meta.model.objects.filter(is_published=True)
    permission_classes = [AllowAny]


class CategoryApiView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = serializer_class.Meta.model.objects.all()
    permission_classes = [AllowAny]