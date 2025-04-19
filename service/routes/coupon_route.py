from rest_framework import generics
from user.permissions import IsAdmin
from service.models.coupon_model import Coupon
from service.serializers.couponserializer import CouponSerializer

class CouponListCreateView(generics.ListCreateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = IsAdmin


class CouponRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    lookup_field = 'id'
    permission_classes = IsAdmin
