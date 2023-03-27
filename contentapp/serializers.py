from rest_framework import serializers
from .models import User
from . models import Content



        
class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'title', 'body', 'summary', 'categories', 'created_by', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_by', 'created_at', 'updated_at']

    def validate_categories(self, value):
        if not value:
            raise serializers.ValidationError('Categories must be provided')
        return value.split(',')
