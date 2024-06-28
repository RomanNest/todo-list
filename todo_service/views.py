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


class TaskCompleteUndoView(generic.UpdateView):
    model = Task
    fields = []
    template_name = "todo_service/task_form.html"
    success_url = reverse_lazy("todo_service:index")

    def get_object(self, queryset=None):
        return get_object_or_404(Task, pk=self.kwargs.get("pk"))

    def form_valid(self, form):
        task = form.save(commit=False)
        task.result = not task.result
        task.save()
        return super().form_valid(form)
