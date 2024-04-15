import uuid
from django.contrib.auth.models import User

from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

class TestBaseAPIView(APITestCase):
    def setUp(self):
        # handle auth
        fake_email = f"{str(uuid.uuid4())}@email.com"
        self.user = User.objects.create(
            email=str(uuid.uuid4()),
        )
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(refresh.access_token)}')
        return super().setUp()