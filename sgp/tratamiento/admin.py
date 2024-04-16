from django.contrib import admin
from .models import Tratamiento, Radiografia

# Register your models here.

class RadiografiaInline(admin.TabularInline):
    model = Radiografia
    extra = 5

class TratamientoAdmin(admin.ModelAdmin):
    inlines = [RadiografiaInline,]      
    readonly_fields = ('created', 'updated')

class RadiografiaAdmin(admin.ModelAdmin): 
    readonly_fields = ('created', 'updated')


admin.site.register(Tratamiento, TratamientoAdmin)
admin.site.register(Radiografia, RadiografiaAdmin)
