from django.contrib import admin

from pizzas.models import Ingredient,Pizza,Comment
# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Pizza)
admin.site.register(Comment)
