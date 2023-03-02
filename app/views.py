from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def skills(request):
    return render(request, "skills.html")
