# Create your views here.

import os

from django.conf import settings
from django.contrib import messages
from django.shortcuts import render
from django.template.response import TemplateResponse


def error(request):
    """Generate an exception. Useful for e.g. configuring Sentry"""
    raise Exception("Make response code 500!")


def current_time(request):
    """Generate the current time. Useful for testing htmx"""
    messages.info(request, "updated the current time")
    return TemplateResponse(request, "current_time.html")


def gallery(request):
    img_path = os.path.join(settings.STATICFILES_DIRS[0], "img/gallery")
    img_list = os.listdir(img_path)
    context = {"images": img_list}
    return render(request, "gallery.html", context)
