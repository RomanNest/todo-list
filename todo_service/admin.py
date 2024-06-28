from django.contrib import admin

from todo_service.models import Tag, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    ordering = ["created_date"]


admin.site.register(Tag)
