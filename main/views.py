from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from datetime import datetime
from django.views.generic import DetailView

from .models import Dish
from .forms import DishForm

# Create your views here.
def homepage(request):
    return render(request = request, 
                  template_name = 'main/home.html',
                  context = {'dishes': Dish.objects.all,
                             'request': request})

def date(request):
    current_datetime = datetime.today()
    return render(request = request,
                  template_name = 'base.html',
                  context = {'current_datetime': current_datetime})

def AboutPage(request):
    return render(request = request,
                  template_name='about/about.html')

def CreateRecipe(request):
    if request.method == 'POST':
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('main:homepage')
            except IntegrityError:
                return render(request, 'main/create_recipe.html', {'form': form, 'title': 'Add a recipe:', 'error_message': 'An error occurred while adding the recipe.'})
    else:
        form = DishForm()
    return render(request, 'main/create_recipe.html', {'form': form, 'title': 'Add a recipe:'})

def AllRecipes(request):
    return render(request=request,
                  template_name='main/all_recipes.html',
                  context={'dishes':Dish.objects.all},
                  )

def RecipeDetail(request, dish_id):
    dish = Dish.objects.select_related(pk=dish_id)
    return render(request=request,
                  template_name='main/recipe_detail.html',
                  context={'dish':dish},
                  )

class RecipeDetailView(DetailView):
    model = Dish
    template_name = 'main/recipe_detail.html'
    