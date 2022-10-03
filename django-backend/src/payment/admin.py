from django.contrib import admin
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'price')
    list_filter = ('id', 'name', 'price')


admin.site.register(Item, ItemAdmin)
