from django.contrib import admin
from django.utils.html import format_html

from .models import (Administrator, Portfolio, Services, SiteSetting, Skill,
                     Summery, Testimonial, WonerTitle)


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
        return format_html(f"<a class='default' href='/admin/main/administrator/{obj.id}/change/'>Change</a>")

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

class servicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'ServiceImage')

    def ServiceImage(self, obj):
        return format_html(f"<img width='100px' height='100px' src='{obj.icon.url}' />")

admin.site.register(Services, servicesAdmin)


class summeryAdmin(admin.ModelAdmin):
    list_display = ('customer', 'project_completed', 'reveiw', 'running_project')

    def has_add_permission(self, obj) -> bool:
        if Summery.objects.all().count() >= 1:
            return False
        else:
            return True

admin.site.register(Summery, summeryAdmin)

class portfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'PortfolioImage')


    def PortfolioImage(self, obj):
        return format_html(f"<img width='100px' height='100px' src='{obj.image.url}' />")
    
    def __str__(self, obj) -> str:
        return obj.title

admin.site.register(Portfolio, portfolioAdmin)

class testimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment', 'ProfileImage')


    def ProfileImage(self, obj):
        if obj.pro_pic:
            return format_html(f"<img width='100px' height='100px' src='{obj.pro_pic.url}' />")
        else: 
            return format_html(f"<img width='100px' height='100px' src='{obj.pro_pic_url}' />")
admin.site.register(Testimonial, testimonialAdmin)

class siteAdmin(admin.ModelAdmin):
    list_display = ('title', 'copy_right', 'bannerBackground', 'skillBackground', 'summeryBackground', 'testimonialBackground', 'contactBackground', 'logo')

    def bannerBackground(self, obj):
        return format_html(f"<img width='100px' src='{obj.banner_bg.url}' />")

    def skillBackground(self, obj):
        return format_html(f"<img width='100px' src='{obj.skill_bg.url}' />")

    def summeryBackground(self, obj):
        return format_html(f"<img width='100px' src='{obj.summery_bg.url}' />")

    def testimonialBackground(self, obj):
        return format_html(f"<img width='100px' src='{obj.testimonial_bg.url}' />")

    def contactBackground(self, obj):
        return format_html(f"<img width='100px' src='{obj.contact_bg.url}' />")

    def logo(self, obj):
        return format_html(f"<img width='100px' src='{obj.site_logo.url}' />")


    def has_add_permission(self, obj) -> bool:
        if SiteSetting.objects.all().count() >= 1:
            return False
        else:
            return True
admin.site.register(SiteSetting, siteAdmin)

class titleAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(WonerTitle, titleAdmin)
