from django.db import models
from ckeditor.fields import RichTextField

class Article(models.Model):
    title = models.CharField(max_length = 500)
    content = RichTextField(blank = True, null = True)    
    cover_image = models.ImageField(upload_to = "media/cover_images/")

    def __str__(self) -> str:
        return self.title