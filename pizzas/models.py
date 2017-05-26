from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_even(value):
    if value > 5  or value < 1 :
        raise ValidationError(
            _('Solo se permite de 1 a 5'),
            params={'value': value},
        )

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(verbose_name=_("Nombre"), max_length=100)
    price = models.DecimalField(verbose_name=_("Precio"), max_digits=6, decimal_places=2)

    def __str__(self): 
        return self.name


class Pizza(models.Model):
    name = models.CharField(verbose_name=_("Nombre"),max_length=100)
    ingredients = models.ManyToManyField(Ingredient,verbose_name=_("Ingredientes"), related_name="pizza")       
    image = models.ImageField(verbose_name=_("Imagen"),null=True, upload_to='img', blank=True)
    description = models.CharField(verbose_name=_("Descripición"),max_length=250, null=True)
    def __str__(self): 
        return self.name
    
class Comment(models.Model):
    text = models.CharField(verbose_name=_("Valoración"),max_length=140)
    created = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(verbose_name=_("Puntuación"),validators=[validate_even])
    pizza = models.ForeignKey(Pizza, verbose_name=_("Pizza"), related_name="comments", related_query_name="comments")
    def __str__(self): 
        return self.text

# def save(self, *args, **kwargs):
#     if self.score > 5:
# 
#         self.score = 5
#    elif self.score < 0:
#        self.score = 0
#    super(Comment, self).save(*args, **kwargs)
        