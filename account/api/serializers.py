from tkinter import S
from rest_framework import serializers
from account.models import User, Register, Profile
from rest_framework.validators import UniqueValidator

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required = True, validators = [UniqueValidator(queryset = User.objects.all())])
    password = serializers.CharField(
        write_only = True,
        required = True,
        style= {'input_type':'password'}
    )
    
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password',
        )

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
        ]

class ProfileCreateSerializer(serializers.ModelSerializer):
    """serializer for creating a account."""
    class Meta:
        model = Profile
        fields = (
            "id",
            "user",
            # "email",
            # "password",
        )

class UserSerializer(serializers.ModelSerializer):
    """serializer for creating a account."""
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
        )

class ProfileRetrieveSerializer(serializers.ModelSerializer):
    """serializer for retrieving a account."""
    user = UserSerializer(read_only = True)
    class Meta:
        model = Profile
        fields = (
            "id",
            "user",
        )
    
    # def get_user(self, obj):
    #     return UserSerializer(self.request.user).data