from django.contrib import admin
from django.utils.html import format_html

from .models import Administrator, Skill


# Register your models here.
class administratorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'title', 'shortDesc', 'position', 'action')
    admin.site.site_title = "Settings"
    


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

class skillAdmin(admin.ModelAdmin):
    list_display = ('title', 'Percentage', 'action')

    def Percentage(self, obj):
        return f"{obj.percentage}%"

    def action(self, obj):
        return format_html(f"<a class='default' href='/admin/main/skill/{obj.id}/change/'>View</a>")

admin.site.register(Skill, skillAdmin)
