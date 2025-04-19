import http.client
import json
from django.conf import settings
from .models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

class GoogleLoginView(APIView):
    def post(self, request):
        access_token = request.data.get("access_token")
        if not access_token:
            return Response({"error": "Access token is required"}, status=400)
        google_api_url = "oauth2.googleapis.com"
        endpoint = f"/tokeninfo?id_token={access_token}"
        
        conn = http.client.HTTPSConnection(google_api_url)
        conn.request("GET", endpoint)
        response = conn.getresponse()

        if response.status != 200:
            return Response({"error": "Invalid Google token"}, status=400)
        data = response.read()
        user_data = json.loads(data.decode("utf-8"))
        email = user_data.get("email")
        name = user_data.get("name")
        user, created = User.objects.get_or_create(
            email=email,
            defaults={
                "username": name,
                "phone_number": "",
            },
        )
        if created:
            user.set_unusable_password()
            user.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
            "user": {"email": user.email, "name": user.username}
        })
