from rest_framework import serializers
from account.models import User,Profile, Register
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
        fields = ('username','email','password',)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email',]

class ProfileCreateSerializer(serializers.ModelSerializer):
    """serializer for creating a account."""
    class Meta:
        model = Profile
        fields = (
            "id",
            "user",
            "email",
            "password",
        )
