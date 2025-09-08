from django.contrib import admin
from .models import Document

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("id", "doc_type", "verification_status", "uploaded_at")
    search_fields = ("doc_type", "verification_status")
