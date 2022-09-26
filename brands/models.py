from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name="напиши имя")

    def __str__(self):
        return self.name



