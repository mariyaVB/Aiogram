from django.contrib import admin
from main.models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent', 'title', 'url', 'named_url', 'menu_name')
    list_display_links = ('id', 'parent', 'title', 'url', 'named_url', 'menu_name')

