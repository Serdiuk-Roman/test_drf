#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from shortly_app.models import Shortly, ShortlyInfo
from shortly_app.serializers import ShortlySerializer, ShortlyInfoSerializer


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    print("ulala+++++++++++++", ip)
    return ip


def base63_encode(number):
    assert number >= 0, 'positive integer required'
    if number == 0:
        return '0'
    alpha = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-'
    base36 = []
    while number != 0:
        number, i = divmod(number, 63)
        base36.append(alpha[i])
    return ''.join(reversed(base36))


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'shortly': reverse('shortly-list', request=request, format=format)
    })


class ShortlyViewSet(viewsets.ModelViewSet):
    queryset = Shortly.objects.all()
    serializer_class = ShortlySerializer

    def perform_create(self, serializer):
        if self.request.user == "AnonymousUser":
            print("##############################")
            serializer.guest = get_client_ip(self.request)
        else:
            serializer.owner = self.request.user
        serializer.save(url_id=base63_encode(Shortly.objects.count() + 1))


class ShortlyInfoViewSet(viewsets.ModelViewSet):
    queryset = ShortlyInfo.objects.all()
    serializer_class = ShortlyInfoSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


def red(request, url_id):
    data = Shortly.objects.get(url_id=url_id)
    try:
        info = ShortlyInfo.objects.get(link=data)
    except ObjectDoesNotExist:
        info = ShortlyInfo(
            link=data,
            guest=request.user,
            click_count=0
        )
    info.guest = request.user
    info.click_count += 1
    info.save()
    return redirect(data.url_target)
