# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Article(models.Model):
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=500)
    body = models.TextField(max_length=5000)
