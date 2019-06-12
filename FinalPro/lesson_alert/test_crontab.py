import random

from django.core.cache import cache
from django.core.mail import send_mail

def test():
        send_mail('Subject here', 'Here is the message.', 'toolsdesu@gmail.com', ['kp3344567@gmail.com'], fail_silently=False)