from django.contrib import admin
from django.utils.html import format_html
from .models.area import Area
from .models.genre import Genre
from .models.restaurant import Restaurant
from django.utils.safestring import mark_safe

#エリア 
class AreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

# ジャンル
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_preview') # 管理画面で表示するフィールド

    def image_preview(self, obj):
        if obj.image:
            return mark_safe('<img src="{}" width="100" />'.format(obj.image.url))
        else:
            return 'No Image'
    image_preview.short_description = 'Image Preview' 

# 店舗   
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'name_alphabet', 'genre', 'address', 'area', 'phone', 'time', 'price_low', 'price_high', 'information', 'image')
    

admin.site.register(Area, AreaAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Restaurant, RestaurantAdmin)