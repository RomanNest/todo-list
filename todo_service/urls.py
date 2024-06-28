from django.urls import path

from todo_service.views import (
    HomePageView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,

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
    ]

app_name = "todo_service"
