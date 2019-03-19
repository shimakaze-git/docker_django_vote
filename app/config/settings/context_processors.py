# coding: utf-8
from django.conf import settings


def common_variables(request):
    return {
        'URL_ROOT': settings.URL_ROOT,
    }
