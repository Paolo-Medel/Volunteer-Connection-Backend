import json
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from volunteerapi.models import JobPosts, VolunteerUsers

class PostsTests(APITestCase):
    fixtures = ['users', 'jobPosts', 'volunteerUsers', 'tokens', 'causeAreas']

    def setUp(self):
        self.user = User.objects.first()
        self.volunteer_user = VolunteerUsers.objects.get(user=self.user)
        token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def test_get_all_posts(self):
        response = self.client.get("/posts")

        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(json_response[0]["id"], 4)
        self.assertEqual(json_response[1]["id"], 3)

    def test_retrieve_post(self):

        post = JobPosts()
        post.title = 'TestPost'
        post.address = '123 way'
        post.image_url = '123.com'
        post.content = 'heloooooo'
        post.user = self.volunteer_user
        post.save()

        response = self.client.get(f"/posts/{post.id}")
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code,status.HTTP_200_OK)

