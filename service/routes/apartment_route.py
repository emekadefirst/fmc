from rest_framework import generics, permissions
from user.permissions import IsAdmin
from service.models.apartment_model import ApartmentType, ExtraSpace
from service.serializers.apartment_serializer import ApartmentTypeSerializer, ExtraSpaceSerializer



class ExtraSpaceViewListCreate(generics.ListCreateAPIView):
    queryset = ExtraSpace.objects.all()
    serializer_class = ExtraSpaceSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdmin()]
        return [permissions.AllowAny()]
    

class ExtraSpaceRetrieveUpdateDestroyAPIViewView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExtraSpace.objects.all()
    serializer_class = ExtraSpaceSerializer
    lookup_field = "id"

    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [IsAdmin()]
        return [permissions.AllowAny()]
    

class ApartmentTypeListCreateView(generics.ListCreateAPIView):
    queryset = ApartmentType.objects.all()
    serializer_class = ApartmentTypeSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdmin()]
        return [permissions.AllowAny()]
    

class ApartmentTypeRetrieveUpdateDestroyAPIViewView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ApartmentType.objects.all()
    serializer_class = ApartmentTypeSerializer
    lookup_field = "id"

    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [IsAdmin()]
        return [permissions.AllowAny()]