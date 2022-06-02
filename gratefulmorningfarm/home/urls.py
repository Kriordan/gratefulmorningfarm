from django.urls import path
from django.views.generic.base import TemplateView

from .views import current_time, error, gallery

urlpatterns = [
    path(r"current-time/", current_time, name="current_time"),
    path(r"error/", error, name="error"),
    path(r"", TemplateView.as_view(template_name="index.html"), name="home"),
    path(r"about", TemplateView.as_view(template_name="about.html"), name="about"),
    path(r"gallery/", gallery, name="gallery"),
    path(r"events", TemplateView.as_view(template_name="events.html"), name="events"),
    path(r"blog", TemplateView.as_view(template_name="blog.html"), name="blog"),
]
