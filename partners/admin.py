from django.contrib import admin

from .models import PartnerCategory, PartnershipOpportunity


@admin.register(PartnerCategory)
class PartnerCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_class', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'description')


@admin.register(PartnershipOpportunity)
class PartnershipOpportunityAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'icon_class', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'description')
