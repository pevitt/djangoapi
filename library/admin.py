from django.contrib import admin
from .models import Author, Editorial, Book
from import_export.admin import ImportExportModelAdmin


# Register your models here.
@admin.register(Author)
class AuthorsAdmin(ImportExportModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'fullname')
    search_fields = ('first_name',)

    def fullname(self, obj):
        return f'{obj.first_name} {obj.last_name}'


@admin.register(Editorial)
class EditorialsAdmin(ImportExportModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name',)
    actions = ["mark_active"]

    def mark_active(self, request, queryset):
        queryset.update(active=False)

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


class AuthorAcquaintanceInline(admin.TabularInline):
    model = Author


@admin.register(Book)
class BooksAdmin(ImportExportModelAdmin):
    list_display = ('name', 'category_book', 'author', 'editorial', 'active')
    raw_id_fields = ("author", "editorial",)
    search_fields = ('name',)
    list_filter = ['category_book', 'editorial']
    readonly_fields = ["name", ]
    list_per_page = 250
    list_editable = ("category_book", "active")
    actions = ["mark_active", "mark_inactive"]

    def mark_active(self, request, queryset):
        queryset.update(active=True)

    def mark_inactive(self, request, queryset):
        queryset.update(active=False)
    # inlines = [AuthorAcquaintanceInline]
