from rest_framework import viewsets

from pizzas.api.serializer import IngredientSerializer,PizzaSerializer,CommentSerializer
from pizzas.models import Ingredient,Pizza,Comment

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [
        # Ejemplo usuario  logeado: IsAuthenticated

    ]

class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    permission_classes = [
        # Ejemplo usuario  logeado: IsAuthenticated
    ]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        # Ejemplo usuario  logeado: IsAuthenticated

    ]  
