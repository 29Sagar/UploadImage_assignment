from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

def validate_image(image):
    file_size = image.size
    print("size-----------",file_size)
    limit_kb = 500
    if file_size > limit_kb * 1024:
        raise ValidationError("Max size of image should be %s KB" % limit_kb)


class UploadImage(models.Model):
    image = models.ImageField('Image', upload_to='image/', blank=True, null=True, validators=[validate_image])

    def __str__(self):
        return self.image # TODO
