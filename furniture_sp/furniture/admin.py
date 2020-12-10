from django.contrib import admin
from .models import Category, Subcategory, Furniture, Gallery
# https://enginetemplates.com/?ref=freemium


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Furniture)
class FurnitureAdmin(admin.ModelAdmin):
    pass


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    pass
