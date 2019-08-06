
from rest_framework import serializers
from uploadapp.models import FileModel

class FileSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = FileModel
        fields = '__all__'
        