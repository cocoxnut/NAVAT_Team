from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Team


class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_image')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('id', 'name',)

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.image.url} width='60', height='65'")


admin.site.register(Team, TeamAdmin)