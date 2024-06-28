from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
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


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_service:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_service:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_service:index")


class TaskCompleteView(generic.RedirectView):
    def post(self, *args, **kwargs):
        task = get_object_or_404(Task, pk=self.kwargs["pk"])
        task.result = True
        task.save()
        return HttpResponseRedirect(reverse_lazy("todo_service:index"))


class TaskUndoView(generic.RedirectView):
    def post(self, *args, **kwargs):
        task = get_object_or_404(Task, pk=self.kwargs["pk"])
        task.result = False
        task.save()
        return HttpResponseRedirect(reverse_lazy("todo_service:index"))
