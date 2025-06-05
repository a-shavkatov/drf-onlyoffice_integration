from django.contrib import admin
from src.apps.documentation.models import Document, Template

# Register your models here.


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "created_at", "updated_at"]
    list_filter = ["created_at", "updated_at"]
    search_fields = ["title"]
    list_per_page = 10

    raw_id_fields = ["owner"]


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
