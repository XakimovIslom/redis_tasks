from django.shortcuts import render
from redis_task.tasks import celery_task
from django.http import HttpResponse


def home_page(request):
    celery_task.delay()
    return HttpResponse("<p>Salom</p>")
