from django.db import models

from conduit.apps.core.models import TimestampedModel


class Article(TimestampedModel):
    title = models.CharField(db_index=True, max_length=255)
    description = models.TextField()
    body = models.TextField()
    image = models.ImageField()
    author = models.ForeignKey(
        'authentication.User', on_delete=models.CASCADE, related_name='articles'
    )

    def __str__(self):
        return self.title


class Comment(TimestampedModel):
    body = models.TextField()

    article = models.ForeignKey(
        'articles.Article', related_name='comments', on_delete=models.CASCADE
    )

    author = models.ForeignKey(
        'authentication.User', related_name='comments', on_delete=models.CASCADE
    )

