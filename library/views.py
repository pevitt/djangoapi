from django.shortcuts import render
from rest_framework import status, permissions, generics, pagination, filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters_django

# models
from .models import Author, Book, Editorial
from .serializers import AuthorSerializer, EditorialSerializer, BookSerializer


# Create your views here.
# Function based crud
@api_view(['GET', 'POST'])
def authors_list_or_create(request):
    if request.method == "GET":
        authors_qs = Author.objects.all()
        author_serializer = AuthorSerializer(authors_qs, many=True)
        return Response(author_serializer.data, status=status.HTTP_200_OK)
    else:
        author_serializer = AuthorSerializer(data=request.data)
        author_serializer.is_valid(raise_exception=True)
        author_serializer.save()
        return Response(author_serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def author_get_or_update(request, pk):
    author = get_object_or_404(Author, id=pk)
    if request.method == "GET":
        author_serializer = AuthorSerializer(author)
        return Response(author_serializer.data, status=status.HTTP_200_OK)
    if request.method == "PUT":
        author_serializer = AuthorSerializer(instance=author, data=request.data)
        author_serializer.is_valid(raise_exception=True)
        author_serializer.save()
        return Response(author_serializer.data, status=status.HTTP_200_OK)
    if request.method == "DELETE":
        author.delete()
        return Response({'msg': 'done'}, status=status.HTTP_204_NO_CONTENT)


# API VIEW CRUD
class EditorialCrud(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk=None, format=None):
        if pk:
            editorial = get_object_or_404(Editorial, id=pk)
            editorial_serializer = EditorialSerializer(editorial)
            return Response(editorial_serializer.data, status=status.HTTP_200_OK)
        else:
            editorial_qs = Editorial.objects.all()
            editorial_serializer = EditorialSerializer(editorial_qs, many=True)
            return Response(editorial_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        editorial_serializer = EditorialSerializer(data=request.data)
        editorial_serializer.is_valid(raise_exception=True)
        editorial_serializer.save()
        return Response(editorial_serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk=None, format=None):
        editorial = get_object_or_404(Editorial, id=pk)
        editorial_serializer = EditorialSerializer(instance=editorial, data=request.data)
        editorial_serializer.is_valid(raise_exception=True)
        editorial_serializer.save()
        return Response(editorial_serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk=None, format=None):
        editorial = get_object_or_404(Editorial, id=pk)
        editorial.delete()
        return Response({'msg': 'done'}, status=status.HTTP_204_NO_CONTENT)


# Generic class-based view crud
# ?search=
class BookCrud(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'category_book']


class BookCrudId(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class CustomPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50
    page_query_param = 'p'


class AuthorFilter(filters_django.FilterSet):
    first_name = filters_django.CharFilter(field_name='first_name', lookup_expr='icontains')


class AuthorCrudGenerics(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['first_name', 'last_name', 'email']
    filterset_class = AuthorFilter
