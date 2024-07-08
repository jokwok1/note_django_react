from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note


# Create your views here.
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated] # must ensure you are logged in

    def get_queryset(self): #easy way to filter the notes made by specific user
        user = self.request.user # get the user that is interacting
        return Note.objects.filter(author=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid(): # check the appropriate validation checks
            serializer.save(author=self.request.user) # save and make new version of note, adding the author
        else:
            print(serializer.errors)
    
class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user 
        return Note.objects.filter(author=user)

class CreateUserView(generics.CreateAPIView): #default creation of view
    queryset = User.objects.all() # list of all the user objects, 
                        #to make sure don't create user that alr exists
    serializer_class = UserSerializer #tells class what data to accept
    permission_classes = [AllowAny] # specify who can call this
