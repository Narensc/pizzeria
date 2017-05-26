from rest_framework import serializers
import json
from pizzas.models import Ingredient,Pizza,Comment


class IngredientSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Ingredient  
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Comment  
        fields = "__all__"

class PizzaSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    comments = CommentSerializer(many=True)
    class Meta: 
        model = Pizza  
        fields = "__all__"

    def create(self, validate_data):
        ingredient_data = self.initial_data.pop['ingredients']
        ingredient_data = json.loads(ingredient_data)
        ingredient_parsed = list(map(lambda c: json.loads(c), ingredient_data))
        validate_data.pop('ingredients')
        validate_data.pop('coments')

        pizza = Pizza.objects.create(**validate_data)

        for ingred in ingredient_data:
            exist = Ingredient.objects.get(name=ingred["name"])
            pizza.ingredients.add(exist)
        return pizza    
