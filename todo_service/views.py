from django.shortcuts import render
from django.views import generic

from todo_service.models import Task, Tag


class HomePageView(generic.ListView):
    model = Task
    template_name = "todo_service/index.html"


# Create your views here.
