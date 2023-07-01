from django.db import models


#By using this File model, you can store information about uploaded files in your application. Each instance of the File model represents a single uploaded file and contains fields to store details such as the file itself, the user who uploaded it, the upload date, the file size, extension, duration, and whether it is a song or not.

# You can perform various operations on the File model objects, such as creating new file instances, retrieving file details, updating file information, and deleting files 


# Create your models here.
class File(models.Model):
    file = models.FileField(upload_to='uploads/')
    user = models.CharField(max_length=255)
    upload_date = models.DateTimeField(auto_now_add=True)
    size = models.CharField(max_length=20)
    extension = models.CharField(max_length=10)
    duration = models.FloatField()
    is_song = models.BooleanField()
