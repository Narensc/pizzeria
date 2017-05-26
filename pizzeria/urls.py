"""pizzeria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include 
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from pizzas.api.views import IngredientViewSet, PizzaViewSet,CommentViewSet


swagger_view= get_swagger_view(title="Pizzeria API")


router_api = routers.DefaultRouter()
router_api.register(r'ingredients', IngredientViewSet)
router_api.register(r'pizzas', PizzaViewSet)
router_api.register(r'comments', CommentViewSet)


api_urlpatterns = [
    url(r'^', include(router_api.urls))

]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(api_urlpatterns)),
    url(r'^docs/', swagger_view),
    url(r'^pizzas/', include("pizzas.urls")),
    url(r'^oauth/', include('social_django.urls', namespace='social')), 
]

