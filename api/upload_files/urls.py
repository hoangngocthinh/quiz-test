from django.urls import path

from upload_files.views import FileUploadAPIView

urlpatterns = [path("", FileUploadAPIView.as_view(), name="upload-files")]
