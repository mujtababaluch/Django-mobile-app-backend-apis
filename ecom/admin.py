from django.contrib import admin
from . import models
from django.utils.html import format_html

# Register your models here.
@admin.register(models.products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'color', 'Category_name', 'display_image')

    def display_image(self, obj):
        return format_html('<img src="{}" alt="Product Image" height="50" />', obj.product_picone.url)
    

    display_image.short_description = 'Image'

admin.site.register(models.Categories)
admin.site.register(models.Size)    