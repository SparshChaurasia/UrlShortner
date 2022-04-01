from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseForbidden
from django.contrib import messages
from .models import Urls


def index(request):
    return render(request, "index.html")


def request(request, name):
    obj = Urls.objects.get(name=name)
    url = getattr(obj, "url")
    return redirect(f"https://{url}")


def new(request):
    if request.method != "POST":
        return HttpResponseForbidden("<b>Invalid request method</b>")

    url = request.POST.get("url")
    name = request.POST.get("name")

    if url and name is None:
        messages.error(request, "Please enter a valid name")
        return redirect("/")

    if Urls.objects.filter(name=name).exists():
        messages.error(request, "This name is already taken")
        return redirect("/")

    u = Urls(name=name, url=url)
    u.save()
    messages.success(request, "Your url was registered successfully")
    messages.info(request, f"Your shortened url is {request.get_host()}/{name}")
    return redirect("/")
