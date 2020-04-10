from celery import Task
from django.conf import settings
from djangoapi.celery import app

from django.conf import settings
from django.template import loader, Context
from django.core.files.base import ContentFile
import base64
from django.core.mail import EmailMessage

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

        send_email = SendEmailTesting()
        testing_data = {
            'testing': "Esto es un correo de prueba",
            'emails': ['jrigoberto17@gmail.com']
        }
        send_email.delay(testing_data, 'library/testing_body.html', 'Probando django')


class SendEmailTesting(Task):
    name = 'Send email testing'

    def run(self, testing_data, template_name, subject_email):
        template_name = template_name
        emails = testing_data['emails']
        subject = subject_email
        global_context = testing_data
        return self.send_email(emails, global_context, subject, template_name)

    @staticmethod
    def send_email(emails, global_context, subject, template_name):
        result = []
        # template = loader.get_template(template_name=template_name)
        # pdf = ContentFile(
        #     base64.urlsafe_b64decode(global_context['pdf']),
        #     'archivo{}.pdf'.format(global_context['year'])
        # )

        try:
            email = EmailMessage(
                subject=subject,
                body="Hola Todos",
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[emails],
            )
            email.content_subtype = "html"
            # if global_context['attach_pdf']:
            # email.attach(pdf.name, pdf.read(), 'application/pdf')
            email.send()
        except Exception:
            raise


app.tasks.register(LibraryTask())
app.tasks.register(SendEmailTesting())
