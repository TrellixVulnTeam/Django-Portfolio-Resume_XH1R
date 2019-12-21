from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<slug:slug>/", views.post_detail, name="project_detail"),
]
