from django.contrib import admin
from .models import Entity, Category, Villain, Hero
from import_export.admin import ImportExportModelAdmin
# Register your models here.
# @admin.register(Entity)
# class EntityAdmin(ImportExportModelAdmin):
#     list_display = ('name', 'gender', 'alternative_name')
#     search_fields = ('name',)
#
@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('name', )
    search_fields = ('name',)

@admin.register(Villain)
class VillainAdmin(ImportExportModelAdmin):
    list_display = ('is_immortal', 'name', 'gender')
    # search_fields = ('name',)

@admin.register(Hero)
class HeroAdmin(ImportExportModelAdmin):
    list_display = ('is_immortal', 'name', 'gender')
    # search_fields = ('name',)
