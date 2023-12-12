from rest_framework import serializers
from rest_framework.validators import ValidationError
from users.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField(max_length=127)
    password = serializers.CharField(max_length=128, write_only=True)
    birthdate = serializers.DateField(required=False)
    is_employee = serializers.BooleanField(default=False, allow_null=True)
    is_superuser = serializers.BooleanField(
        default=False,
        allow_null=True,
        read_only=True
    )

    def validate_email(self, value):
        if User.objects.filter(email=value).first():
            raise ValidationError("email already registered.")
        return value

    def validate_username(self, value):
        if User.objects.filter(username=value).first():
            raise ValidationError("username already taken.")
        return value

    def create(self, validated_data):
        if ((validated_data["is_employee"] is None)
           or (validated_data["is_employee"] is False)):
            user = User.objects.create_user(**validated_data)
        else:
            validated_data["is_superuser"] = True
            user = User.objects.create_superuser(
                **validated_data
            )
        return user

    def update(self, instance: User, validated_data):
        for key, value in validated_data.items():
            if key == "password" and value:
                instance.set_password(value)
            else:
                setattr(instance, key, value)
        instance.save()
        return instance


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128)
