from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from .views import (
    ArticleViewSet, CommentsListCreateAPIView
)

router = DefaultRouter()
router.register(r'articles', ArticleViewSet, base_name='articles')

urlpatterns = router.urls
