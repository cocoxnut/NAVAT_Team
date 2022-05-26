from django.db import models

class Food(models.Model):
    title = models.CharField(max_length=45, verbose_name='Name of food')
    author = models.CharField(max_length=35, verbose_name='from author')
    description = models.TextField()
    image = models.ImageField(upload_to='food/%Y/%m')

    class Meta:
        verbose_name_plural = 'Food'


# Create your models here.
