#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.db import models


class Shortly(models.Model):
    url_id = models.CharField(max_length=6, unique=True, editable=False)
    url_target = models.URLField(max_length=250, unique=True)
    guest = models.CharField(max_length=32, blank=True, null=True)
    owner = models.ForeignKey(
        'auth.User',
        related_name='shortlies',
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
    deleted = models.BooleanField(default=False)


class ShortlyInfo(models.Model):
    link = models.OneToOneField(
        Shortly,
        on_delete=models.CASCADE,
        related_name='link')
    guest = models.CharField(max_length=32, blank=True, null=True)
    last_datetime = models.DateTimeField(auto_now=True)
    click_count = models.PositiveSmallIntegerField(default=0)
