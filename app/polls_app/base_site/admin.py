from django.contrib import admin
from django.contrib.sites.models import Site
from .models import SiteDetail

# Register your models here.


class SiteDetailInline(admin.StackedInline):
    """サイト詳細情報のインライン"""
    model = SiteDetail


class SiteAdmin(admin.ModelAdmin):
    """Siteモデルを、管理画面でSiteDetailもインラインで表示できるように"""
    inlines = [SiteDetailInline]

admin.site.unregister(Site)
admin.site.register(Site, SiteAdmin)
