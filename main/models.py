from django.db import models
from django.contrib.auth.models import AbstractUser

class Category(models.Model):
    name:str = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural:str  = "Categories"

    def __str__(self) -> str:
        return self.name


class Quote(models.Model):
    category:Category = models.ForeignKey(Category,on_delete=models.CASCADE)
    quote:str = models.TextField()
    favorite:bool = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.quote

