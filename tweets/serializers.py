from rest_framework import serializers
from .models import Tweet
class TweetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tweet
        fields = ['name', 'message', 'created_at']