from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("Portfolio/", views.index, name="index"),
    path("skills/", views.skills, name="skills"),
    path("admin/", admin.site.urls),
]
