from django.db import models

# Create your models here.

class UploadLog(models.Model):
    filename = models.CharField(max_length=255)
    uploaded_by = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.filename
