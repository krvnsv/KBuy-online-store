from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import render

def say_hello(request):
    try:
        # send_mail('subject', 'message', 'info@kbuy.com', ['bob@kbuy.com'])
        # mail_admins('subject', 'message', html_message='message')
        message = EmailMessage('subject', 'message', 'from@kbuy.com', ['john@kbuy.com'])
        message.attach_file('playground/static/images/dog.jpg')
        message.send()
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Kirill',})
