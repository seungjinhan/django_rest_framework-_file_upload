from django.conf.urls import url
from uploadapp.views import FileView


urlpatterns = [
    url('', FileView.as_view(), name="file-upload")
]