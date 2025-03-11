from django.contrib import admin
from .models import Profile, Ingredient, PotionUse, Potion, PotionIngredient
# Register your models here.

admin.site.register(Profile)
admin.site.register(Ingredient)
admin.site.register(PotionUse)
admin.site.register(Potion)
admin.site.register(PotionIngredient)
