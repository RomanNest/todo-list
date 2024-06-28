from django.urls import path

from todo_service.views import (
    HomePageView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskCompleteView,
    TaskUndoView,
)


urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path(
        "tags/",
        TagListView.as_view(),
        name="tag-list",
    ),
    path("tags/create/",
         TagCreateView.as_view(),
         name="tags-create",
         ),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tags-update",
    ),
    path(
        "tags/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tags-delete",
    ),
    path(
        "tasks/create/",
        TaskCreateView.as_view(),
        name="task-create",
    ),
    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update",
    ),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete",
    ),
    path(
        "complete_tasks/<int:pk>/",
        TaskCompleteView.as_view(),
        name="complete-task",
    ),
    path(
        "undo_tasks/<int:pk>/",
        TaskUndoView.as_view(),
        name="undo-task",
    ),
    ]

app_name = "todo_service"
