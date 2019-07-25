# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-07-24 22:26
from __future__ import unicode_literals

from io import BytesIO
from urllib.parse import urlparse

import requests
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import migrations
from mixer.backend.django import mixer

from conduit.apps.articles.models import Article, Comment


def get_remote_image():
    image_url = "https://picsum.photos/860/400"
    im = None
    r = requests.get(image_url, stream=True)
    if r.status_code == 200:
        name = "1.jpg"
        i = Image.open(r.raw)
        buffer = BytesIO()
        if i.mode != "RGB":
            i = i.convert("RGB")
        i.thumbnail((500, 500), Image.ANTIALIAS)
        i.save(buffer, format='JPEG')
        im = InMemoryUploadedFile(
            buffer,
            None,
            name,
            'image/jpeg',
            buffer.tell(),
            None)

    yield im


def create_lorem_ipsum_articles(apps, schema_editor):
    articles = mixer.cycle(20).blend(Article, image=get_remote_image)
    for article in articles:
        mixer.cycle(5).blend(Comment, article=article)


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_lorem_ipsum_articles),
    ]