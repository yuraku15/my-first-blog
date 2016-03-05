from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    autora = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=400)
    contenido = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo 
