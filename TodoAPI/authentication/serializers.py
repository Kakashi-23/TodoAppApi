from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=30, min_length=5)
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=30, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    # def validate(self, attrs):
    #     email = attrs.get('email', '')
    #     if User.objects.filter(email=email).exists():
    #         raise serializers.ValidationError({
    #             'email': 'Email already exists'
    #         })
    #     return super().validate(attrs)

    def create(self, validated_data):
        user = User(email=validated_data['email'],
                    username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user


class LoginSerializer(serializers.ModelSerializer):
    #  username = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=30, min_length=5)
    password = serializers.CharField(max_length=30, min_length=6)

    class Meta:
        model = User
        fields = ['email', 'password']
