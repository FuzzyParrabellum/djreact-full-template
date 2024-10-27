from rest_framework import serializers

from core.users.models import User
from .models import Note


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
    
class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}
    
