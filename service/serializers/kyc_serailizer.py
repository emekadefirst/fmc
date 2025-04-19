from rest_framework import serializers
from user.models import User
from service.models.kyc_model import UserKYCProfile


class UserKYCProfileSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="email", queryset=User.objects.all())
    class Meta:
        model = UserKYCProfile
        fields = ['id', 'user', 'fullname', 'phone_number', 'id_image', 'resume', 'id_document', 'status', 'created_at', 'updated_at']
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }

    def create(self, validated_data):
        return UserKYCProfile.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()  
        return instance
    
