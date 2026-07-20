from django.contrib import admin

from .models import Project, ProjectCategory


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('label', 'slug', 'order')
    list_editable = ('order',)
    prepopulated_fields = {'slug': ('label',)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_featured', 'order', 'is_active')
    list_filter = ('category', 'is_featured', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'description', 'location')
