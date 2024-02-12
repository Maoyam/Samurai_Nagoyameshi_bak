from django.contrib import admin
from .models.area import Area
from .models.genre import Genre
from django.utils.safestring import mark_safe

class AreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_preview')
    readonly_fields = ('image_preview',)
    
    def image_preview(self, obj):
        return obj.image.url if obj.image else None
    image_preview.short_description = 'Image Preview'

admin.site.register(Area, AreaAdmin)
admin.site.register(Genre, GenreAdmin)