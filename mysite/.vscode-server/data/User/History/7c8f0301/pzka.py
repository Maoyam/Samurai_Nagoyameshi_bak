from django.contrib import admin
from .models.area import Area
from django.utils.safestring import mark_safe
from .models.genre import Genre

class AreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')


admin.site.register(Area, AreaAdmin)
admin.site.register(Genre, GenreAdmin)