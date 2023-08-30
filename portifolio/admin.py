from django.contrib import admin
from portifolio.models import Projects, ImageFieldsProject

class AdminProjects(admin.ModelAdmin):
    list_display = ("id", "title", "category", "public_project")
    list_display_links = ("id", "title")
    search_fields = ("title",)
    list_filter = ("category", "public_project",)
    list_editable = ("public_project",)
    list_per_page = 10


admin.site.register(Projects, AdminProjects)


class ImgFieldsProjects(admin.ModelAdmin):
    list_display = ("id", "project")
    list_display_links = ("id", "project")
    search_fields = ("project",)
    list_filter = ("project",)
    list_per_page = 10

admin.site.register(ImageFieldsProject, ImgFieldsProjects)