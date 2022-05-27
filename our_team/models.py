from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=25, verbose_name='Name of staff')
    description = models.TextField(verbose_name='Briefly about')
    image = models.ImageField(upload_to='team/%Y/%m', blank=True)

    class Meta:
        verbose_name_plural = 'Team'
