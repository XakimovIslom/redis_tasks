from django.urls import path
from redis_task import views

urlpatterns = [
    path("", views.home_page)
]