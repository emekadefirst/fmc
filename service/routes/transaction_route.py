from rest_framework import generics, permissions
from user.permissions import IsAdmin
from service.models.transaction_model import BookingPayment, Payout
from service.serializers.transaction_serializer import BookingPaymentSerializer, PayoutSerializer


class BookingPaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookingPayment.objects.all()
    serializer_class = BookingPaymentSerializer
    lookup_field = 'id'
    permission_classes = IsAdmin

class BookingPaymentListView(generics.ListCreateAPIView):
    queryset = BookingPayment.objects.all()
    serializer_class = BookingPaymentSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdmin()]
        return [permissions.AllowAny()]

class PayoutDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payout.objects.all()
    serializer_class = PayoutSerializer
    lookup_field = 'id'
    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdmin()]
        return [permissions.AllowAny()]

class PayoutListView(generics.ListCreateAPIView):
    queryset = Payout.objects.all()
    serializer_class = PayoutSerializer
    permission_classes = IsAdmin