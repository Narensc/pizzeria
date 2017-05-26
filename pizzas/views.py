from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from pizzas.models import Pizza
from django.http import Http404
# Create your views here.

def index(request):
    pizza_list = Pizza.objects.all()
#   html = ''
#  for pizza in pizza_list:
#     url = '/pizzas/' + str(pizza.id) + '/'
#     html += '<a href="' + url + '">' + pizza.name + '</a> <br>' 
#    return HttpResponse(html)
    #return HttpResponse ("<p>This is the home page for the PizzaShop Web application. </p> <p>To prove that they work, you can execute either of the following links: <ul> <li>To a <a href='http://127.0.0.1:8000/admin/'>Admin Login</a>. <li>To a <a href='http://127.0.0.1:8000/api/v1/'>Api</a>. </ul>" )
#    template =  loader.get_template('pizza/index.html')

    context = {
        'pizza_list': pizza_list
    }
#    return HttpResponse(template.render(context, request))

    return render(request, 'pizza/index.html', context)


def detail (request, pizza_id):
    try:
        pizza = Pizza.objects.get(pk=pizza_id)
    except Pizza.DoesNotExist:
        raise Http404 ("Esta pizza no existe")    
    #return HttpResponse("<h2> Detalles de la pizza " + str(pizza_id) + "</h2>") 
       
    return render(request, 'pizza/detail.html', context={'pizza':pizza})
    
def conocenos(request):
    return HttpResponse ("<h1> Pizzeria online </h1> <h2> Crea tus pizzas al gusto </h2>")

def fichero(request):
    template = loader.get_template('pizza/fichero.html')
    context = { }
    return HttpResponse(template.render(context, request))
    #return render(request, 'pizza/fichero.html')
       
