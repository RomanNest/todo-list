from django.urls import path

from todo_service.views import (
    HomePageView,
)


urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    ]

app_name = "todo_service"
