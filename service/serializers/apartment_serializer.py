from rest_framework import serializers
from service.models.apartment_model import ApartmentType, ExtraSpace


class ApartmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentType
        fields = ['id', 'name', 'number_of_room', 'number_of_bathroom', 'price', 'in_kitchen', 'created_at', 'updated_at']
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }

    def create(self, validated_data):
        return ApartmentType.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()  
        return instance
    

class ExtraSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraSpace
        fields = ['id', 'name', 'price', 'created_at', 'updated_at']
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }

    def create(self, validated_data):
        return ExtraSpace.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()  
        return instance