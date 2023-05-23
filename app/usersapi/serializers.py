from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email', 'password']
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user 


class UserLoginSerialzer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=16, min_length=8)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user 
        return serializers.ValidationError("Invalid username or password.")

