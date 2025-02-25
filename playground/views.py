from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage

def say_hello(request):
    try:
        message = BaseEmailMessage(
            template_name='emails/hello.html',
            context={'name': 'Kirill'}
        )
        message.send(['john@kbuy.com'])
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Kirill',})
