from django.urls import include, path
from .views import author_get_or_update, authors_list_or_create, EditorialCrud, BookCrud, BookCrudId, AuthorCrudGenerics

urlpatterns = [
    path(
        'authors',
        authors_list_or_create,
        name="authors_list_or_create"
    ),
    path(
        'authors/<int:pk>/',
        author_get_or_update,
        name="author_get_or_update"
    ),
    path(
        'editorials',
        EditorialCrud.as_view(),
        name="editorial_list_or_create"
    ),
    path(
        'editorials/<int:pk>/',
        EditorialCrud.as_view(),
        name="editorial_get_or_update"
    ),
    path(
        'books',
        BookCrud.as_view(),
        name="book_list_or_create"
    ),
    path(
        'books/<int:pk>/',
        BookCrudId.as_view(),
        name="book_get_or_update"
    ),
    path(
        'author',
        AuthorCrudGenerics.as_view(),
        name="author_list_or_create"
    )
]