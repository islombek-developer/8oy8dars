from django.contrib import admin
from .models import Food,FoodType,Comment


class FoodAdmin(admin.ModelAdmin):
    list_display = ('pk','foodtype','name','price','tarkibi')

admin.site.register(Food,FoodAdmin)
admin.site.register(FoodType)
admin.site.register(Comment)