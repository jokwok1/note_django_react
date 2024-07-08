from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

# Object relational mapping, django will help with the DB management

# serializers to take in json data to convert to object

#Inherit from the ModelSerializer class
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"] # attributes we want to serialize
        extra_kwargs = {"password" : {"write_only" : True}} 
        # accept password when creating user, but not returning pw when getting information 
    
    # Method to create user, pass the validated data
    def create(self, validated_data): 
        user = User.objects.create_user(**validated_data)
        return user
    
class NoteSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}
        # only can read who the author is, can't write since it should be done automatically based on who logged in
        