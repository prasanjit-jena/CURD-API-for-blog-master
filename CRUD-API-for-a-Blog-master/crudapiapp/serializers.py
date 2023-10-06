from rest_framework import serializers
from .models import BlogData

class BlogDataSerializer(serializers.ModelSerializer):
    blog_id=serializers.ReadOnlyField()
    class Meta:
        model=BlogData
        fields="__all__"