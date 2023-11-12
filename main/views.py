from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from datetime import datetime
from django.views.generic import DetailView
from django.core.paginator import Paginator

from .models import Dish
from .forms import DishForm

# Create your views here.
def homepage(request):
    dish_list = Dish.objects.all()
    paginator = Paginator(dish_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request = request, 
                  template_name = 'main/home.html',
                  context = {'page_obj':page_obj,
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
    dish_list = Dish.objects.all()
    paginator = Paginator(dish_list, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request=request,
                  template_name='main/all_recipes.html',
                  context={'page_obj':page_obj,
                  }
                  )


class RecipeDetailView(DetailView):
    model = Dish
    template_name = 'main/recipe_detail.html'
    
