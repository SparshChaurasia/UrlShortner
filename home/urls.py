from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("xwCgCNirsq", views.new, name="new"),
    path("<str:name>", views.request)
]
