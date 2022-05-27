from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Food


class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'get_image')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('author',)
    ordering = ('id','title',)

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.image.url} width='60', height='50'")

admin.site.register(Food, FoodAdmin)
