from django.db import models

# Create your models here.
class UploadModel(models.Model):
    # file will be uploaded to MEDIA_ROOT/uploads
    # or...
    # file will be saved to MEDIA_ROOT/uploads/2015/01/30
    upload = models.FileField(upload_to='files',null=True)