import json
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.test import APITestCase
from volunteerapi.models import VolunteerUsers

class VolunteerTests(APITestCase):

    fixtures = ['causeAreas', 'users', 'tokens', 'volunteerUsers', 'jobPosts']

    def setUp(self):
        token = Token.objects.first()
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def test_get_rare_user(self):

        response = self.client.get(f"/volunteers/{3}")

        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(json_response["bio"], "bio 3")
        self.assertEqual(json_response["profile_image_url"], "https://www.example.com/profile3.jpg")
        self.assertEqual(json_response["created_on"], "2022-12-01T08:30:00Z")
        self.assertEqual(json_response["is_business"], False)
        self.assertEqual(json_response["favorite"], [])
        self.assertEqual(json_response["user"]["full_name"], "Jenna Solis")
        self.assertEqual(json_response["user"]["email"], "jenna@solis.com")
        self.assertEqual(json_response["user"]["username"], "jenna@solis.com")
        self.assertEqual(json_response["cause_area"][0]["id"], 2)
        self.assertEqual(json_response["cause_area"][0]["label"], "Children")

    def test_get_volunteers(self):
        response = self.client.get("/volunteers")

        json_response = json.loads(response.content)

        self.assertIsNotNone(json_response[0])
        self.assertIsNotNone(json_response[1])
        self.assertIsNotNone(json_response[2])
        self.assertIsNotNone(json_response[3])
        self.assertIsNotNone(json_response[4])