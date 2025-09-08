from rest_framework import serializers
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"
        read_only_fields = ["uploaded_at", "updated_at", "raw_extracted"]  # ✅ keep OCR data read-only
