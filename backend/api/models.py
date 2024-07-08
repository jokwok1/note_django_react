from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # automatically records the timestamp when an object is created
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    # each instance of the model containing this field (author) is associated with a single instance of the User model
    # on_delete=models.CASCADE: This specifies the behavior when the referenced User object is deleted. CASCADE ensures that when the referenced User is deleted, 
    # all related objects (in this case, notes) are also deleted
    # related_name="notes": This is used to define the reverse relation from User to your model. It allows you to access related MyModel instances from a User 
    # instance using the specified name (notes

    def __str__(self):
        return self.title