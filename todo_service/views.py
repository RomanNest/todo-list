from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo_service.models import Task, Tag


class HomePageView(generic.ListView):
    model = Task
    template_name = "todo_service/index.html"


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_service:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_service:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_service:tag-list")
