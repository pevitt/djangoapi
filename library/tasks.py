from celery import Task
from django.conf import settings
from djangoapi.celery import app

from .models import Editorial


class LibraryTask(Task):
    name = "Testing Task"

    def run(self, *args, **kwargs):
        print(args)

        return self.get_library()

    def get_library(self):
        editorial = Editorial.objects.get(pk=2)
        editorial.name = "Santillada Espanola"
        editorial.save()

app.tasks.register(LibraryTask())