from django.contrib import admin
from .models.area import Area
from django.utils.safestring import mark_safe

class AreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Area, AreaAdmin)