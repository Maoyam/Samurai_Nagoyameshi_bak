from django.contrib import admin
from .models.area import Area
from .models.genre import Genre
from django.utils.safestring import mark_safe

class AreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')
    
    def image(self, obj):
         return mark_safe('<img src="{}">'.format(obj.img.url))

admin.site.register(Area, AreaAdmin)
admin.site.register(Genre, GenreAdmin)