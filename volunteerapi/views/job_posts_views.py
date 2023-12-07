from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from volunteerapi.models import CauseAreas, Favorites, UserCause

class UserSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()

    def get_author_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    
    class Meta:
        model = User
        fields = ('author_name',)
