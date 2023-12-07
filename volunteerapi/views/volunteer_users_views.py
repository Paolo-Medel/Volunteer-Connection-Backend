from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.contrib.auth.models import User
from volunteerapi.models import VolunteerUsers, CauseAreas, JobPosts


class VolunteerUsersView(ViewSet):
    """Viewset for volunteer_users"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single game

        Returns:
            Response -- JSON serialized game instance
        """
        volunteer_user = VolunteerUsers.objects.get(pk=pk)
        serialized = VolunteerUsersSerializer(volunteer_user)
        return Response(serialized.data)


    def list(self, request):
        """Handle GET requests to volunteer_users resource

        Returns:
            Response -- JSON serialized list of volunteer_users
        """
        volunteer_users = VolunteerUsers.objects.all()
        serialized = VolunteerUsersSerializer(volunteer_users, many=True)
        return Response(serialized.data)

class UserVolunteerUsersSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    def get_email(self, obj):
        return f'{obj.username}'

    def get_full_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'

    class Meta:
        model = User
        fields = ('full_name', 'email', 'username')

class FavoritesVolunteerUsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobPosts
        fields = ('title', 'content', 'address', 'publication_date')

class CauseAreaVolunteerUsersSerializers(serializers.ModelSerializer):

    class Meta:
        model = CauseAreas
        fields = ('id', 'label')

class VolunteerUsersSerializer(serializers.ModelSerializer):
    user = UserVolunteerUsersSerializer(many=False)
    cause_area = CauseAreaVolunteerUsersSerializers(many=True)
    favorite = FavoritesVolunteerUsersSerializer(many=True)

    class Meta:
        model = VolunteerUsers
        fields = ('id', 'bio', 'profile_image_url', 'created_on', 'user', 'is_business', 'cause_area', 'favorite')
