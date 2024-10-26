from core.users.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """Serializes user data"""
    
    class Meta:
        model = User
        fields = ['id', 'email', 'password']
        # indicates below that doesn't want to be returned password info when
        # querying user info, later after user creation.
        extra_kwargs = {"password": {"write_only":True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user