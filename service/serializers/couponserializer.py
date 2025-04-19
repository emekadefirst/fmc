from rest_framework import serializers
from service.models.coupon_model import Coupon

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ['id', 'code', 'name', 'discount', 'start_time', 'end_time', 'validity', 'created_at', 'updated_at']
        read_only_fields = ['id', 'code', 'created_at', 'updated_at']

    def create(self, validated_data):
        return Coupon.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()  
        return instance
