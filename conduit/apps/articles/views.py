from rest_framework import generics, mixins, status, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.permissions import (
    AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
)
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Article
from .renderers import ArticleJSONRenderer
from .serializers import ArticleSerializer, CreateCommentSerializer


class ArticleViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CommentsListCreateAPIView(mixins.CreateModelMixin,
                                viewsets.GenericViewSet):
    serializer_class = CreateCommentSerializer

