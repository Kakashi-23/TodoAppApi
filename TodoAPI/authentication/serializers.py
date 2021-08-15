from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    username = serializers.EmailField(max_length=30)
    email = serializers.EmailField(max_length=30, min_length=5)
    first_name = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=30, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'email', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({
                'email': 'Email already exists'
            })
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    #  username = serializers.CharField(max_length=30)
    username = serializers.EmailField(max_length=30, min_length=5)
    password = serializers.CharField(max_length=30, min_length=6)

    class Meta:
        model = User
        fields = ['username', 'password']
