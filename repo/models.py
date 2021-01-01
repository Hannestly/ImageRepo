from django.db import models
from django.templatetags.static import static
# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=200)
    tag = models.TextField(null=True)
    description = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    image_path = models.TextField(null=True,blank=True)

    @property
    def img_url(self):
        return static(self.image_path)

    def __str__(self):
        return self.title