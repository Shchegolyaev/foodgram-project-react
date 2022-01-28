from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password')

    def create(self, validated_data):
        return User.objects.get_or_create(**validated_data)[0]

    def validate_username(self, value):
        if value == "me":
            raise serializers.ValidationError("me - недопустимый username")
        return value

