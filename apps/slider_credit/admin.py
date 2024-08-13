from django.contrib import admin
from .models import Slider, Credit

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)

@admin.register(Credit)
class CreditAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'amount', )
    search_fields = ('name', 'amount')
