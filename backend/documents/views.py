from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Document
from .serializers import DocumentSerializer
from .utils import extract_text_from_file, dummy_field_parser

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all().order_by("-uploaded_at")
    serializer_class = DocumentSerializer

    def perform_create(self, serializer):
        document = serializer.save()
        text = extract_text_from_file(document.file)
        parsed = dummy_field_parser(text)

        document.raw_extracted = parsed
        document.save()

    @action(detail=True, methods=["post"])
    def verify(self, request, pk=None):
        document = self.get_object()
        normalized_data = request.data.get("normalized_data")
        status_value = request.data.get("verification_status", "verified")

        if normalized_data:
            document.normalized_data = normalized_data
            document.verification_status = status_value
            document.save()

            return Response(
                {"message": "Document verified & corrected", "document": DocumentSerializer(document).data},
                status=status.HTTP_200_OK,
            )

        return Response({"error": "normalized_data required"}, status=status.HTTP_400_BAD_REQUEST)
