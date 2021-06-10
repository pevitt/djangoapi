from django.db import models


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.first_name


class Editorial(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    logo = models.ImageField(null=True, blank=True, upload_to="avatars")
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    CATEGORY_CHOICES = (
        ('infaltil', 'Infantil'),
        ('terror', 'Terror'),
        ('novela', 'Novela'),
        ('documental', 'Documental'),
    )

    name = models.CharField(max_length=100)
    category_book = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=True, null=True,
                                     default='documental')
    logo = models.ImageField(null=True, blank=True, upload_to="avatars")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    book_pdf = models.FileField(upload_to="documentos")
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
