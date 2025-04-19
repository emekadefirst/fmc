from rest_framework import serializers
from service.models.booking_model import BookingDetail
from service.models.transaction_model import BookingPayment, Payout



class BookingPaymentSerializer(serializers.ModelSerializer):
    booking_id = serializers.SlugRelatedField(slug_field="id", queryset=BookingDetail.objects.all())
    class Meta:
        model = BookingPayment
        fields = ['id', 'booking_id', 'cleaner', 'client', 'amount', 'promo_code', 'discounted', 'transation_id', 'status', 'created_at', 'updated_at']
        extra_kwargs = {
            'id': {'read_only': True},
            'booking_id': {'read_only': True},
            'cleaner': {'read_only': True},
            'client': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }

    def create(self, validated_data):
        return BookingPayment.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()  
        return instance
    

class PayoutSerializer(serializers.ModelSerializer):
    booking_id = serializers.SlugRelatedField(slug_field="id", queryset=BookingDetail.objects.all())
    class Meta:
        model = Payout
        fields = ['id', 'booking_id', 'cleaner', 'amount',  'transation_id', 'status', 'created_at', 'updated_at']
        extra_kwargs = {
            'id': {'read_only': True},
            'booking_id': {'read_only': True},
            'client': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }

    def create(self, validated_data):
        return Payout.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()  
        return instance
    