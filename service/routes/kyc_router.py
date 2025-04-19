from rest_framework import generics, permissions
from user.permissions import IsAdmin
from service.models.kyc_model import UserKYCProfile
from service.serializers.kyc_serailizer import UserKYCProfileSerializer

class UserKYCProfileListCreateView(generics.ListCreateAPIView):
    queryset = UserKYCProfile.objects.all()
    serializer_class = UserKYCProfileSerializer
    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.AllowAny()]
        return [IsAdmin()]

class UserKYCProfileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserKYCProfile.objects.all()
    serializer_class = UserKYCProfileSerializer
    lookup_field = 'id'
    permission_classes = IsAdmin

