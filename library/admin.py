from django.contrib import admin
from .models import Author, Editorial, Book
from import_export.admin import ImportExportModelAdmin


# Register your models here.
@admin.register(Author)
class AuthorsAdmin(ImportExportModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name',)


@admin.register(Editorial)
class EditorialsAdmin(ImportExportModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name',)


@admin.register(Book)
class BooksAdmin(ImportExportModelAdmin):
    list_display = ('name', 'category_book', 'author', 'editorial')
    raw_id_fields = ("author",)
    search_fields = ('name',)
    list_filter = ['category_book', 'editorial']
