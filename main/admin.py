from django.contrib import admin
from django.utils.html import format_html

from .models import Administrator

# Register your models here.

class administratorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'title', 'shortDesc', 'position', 'action')
    site_header = "Administrator settings"

    def shortDesc(self, obj):
        if len(obj.short_desc) > 300:
            return f"{obj.short_desc[:300]}..."
        else:
            return obj.short_desc

    def action(self, obj):
        return format_html(f"<a class='default' href='/admin/main/administrator/{obj.id}/change/'>View</a>")

    def has_add_permission(self, obj) -> bool:
        if Administrator.objects.all().count() >= 1:
            return False
        else:
            return True

   

admin.site.register(Administrator, administratorAdmin)
