from rest_framework import serializers

from upload_files.models import UploadedFile


class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ("id", "file")

    def validate(self, attributes):
        if attributes["file"]:
            attributes["name"] = attributes["file"].name
            attributes["file_size"] = attributes["file"].size
            attributes["file_type"] = attributes["file"].content_type
        return attributes
