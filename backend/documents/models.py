from django.db import models
from django.contrib.auth import get_user_model
from .utils import extract_text_from_file  # import the OCR function

User = get_user_model()

class Document(models.Model):
    DOC_TYPES = [
        ("aadhaar", "Aadhaar"),
        ("pan", "PAN"),
        ("dl", "Driver License"),
        ("marksheet", "Marksheet"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    doc_type = models.CharField(max_length=20, choices=DOC_TYPES)
    file = models.FileField(upload_to="documents/")

    # extracted JSON from OCR
    raw_extracted = models.JSONField(null=True, blank=True)
    # manually corrected/normalized fields
    normalized_data = models.JSONField(null=True, blank=True)

    verification_status = models.CharField(
        max_length=20,
        choices=[("pending", "Pending"), ("verified", "Verified"), ("rejected", "Rejected")],
        default="pending",
    )

    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_doc_type_display()} ({self.id})"
    

class Document(models.Model):
    DOC_TYPES = [
        ("aadhaar", "Aadhaar"),
        ("pan", "PAN"),
        ("dl", "Driver License"),
        ("marksheet", "Marksheet"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    doc_type = models.CharField(max_length=20, choices=DOC_TYPES)
    file = models.FileField(upload_to="documents/")

    raw_extracted = models.JSONField(null=True, blank=True)
    normalized_data = models.JSONField(null=True, blank=True)

    verification_status = models.CharField(
        max_length=20,
        choices=[("pending", "Pending"), ("verified", "Verified"), ("rejected", "Rejected")],
        default="pending",
    )

    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # save file first
        if not self.raw_extracted:  # only extract if empty
            text = extract_text_from_file(self.file.path)
            self.raw_extracted = {"text": text}
            super().save(update_fields=["raw_extracted", "updated_at"])

    def __str__(self):
        return f"{self.get_doc_type_display()} ({self.id})"

