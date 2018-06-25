#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from django.contrib.auth.models import User
from rest_framework import serializers
from shortly_app.models import Shortly, ShortlyInfo  # Snippet


class ShortlySerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Shortly
        fields = ('url_id', 'url_target', 'guest', 'owner')


class ShortlyInfoSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ShortlyInfo
        fields = '__all__'
