from django.shortcuts import render
import random
from .models import Category, Subcategory, Furniture


def main(request):
    categories = Category.objects.all()
    furniture = Furniture.objects.all()
    featured_id = furniture.filter(featured=True).values_list("id", flat=True)
    featured_rnd_id = random.sample(list(featured_id), 4)
    featured = furniture.filter(id__in=featured_rnd_id)
    return render(request, 'furniture/home.html', {'furniture': furniture,
                                                   'categories': categories,
                                                   'featured': featured,
                                                   })


def dtl_furniture(request, pk):
    sng_frn = Furniture.objects.get(id=pk)
    return render(request, 'furniture/dtl_furniture.html', {'sng_frn': sng_frn})


def all_subcategories(request):
    subcategories = Subcategory.objects.all()
    return render(request, 'furniture/home.html', {'subcategories': subcategories})


def checkout(request):
    return render(request, 'furniture/checkout.html')
