from django.contrib import admin

from app.models import Category, Product, Tag
from advanced_filters.admin import AdminAdvancedFiltersMixin

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name']

class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class ProductAdmin(AdminAdvancedFiltersMixin, admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'get_tags']
    list_filter = ['is_active']
    search_fields = ['name']

    advanced_filter_fields = (
        ('category__name', 'Categoria - Nome'),
        ('tags__name', 'Tag - Nome'),
    )

    def get_tags(self, obj):
        return ", ".join([t.name for t in obj.tags.all()])

    get_tags.short_description = 'tags'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Product, ProductAdmin)