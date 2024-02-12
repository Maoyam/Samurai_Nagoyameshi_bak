from django.contrib import admin
from .models.area import Area
from .models.genre import Genre
from django.utils.safestring import mark_safe

class AreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_preview') # 管理画面で表示するフィールド

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        else:
            return 'No Image'
    image_preview.short_description = 'Image Preview' 

admin.site.register(Area, AreaAdmin)
admin.site.register(Genre, GenreAdmin)