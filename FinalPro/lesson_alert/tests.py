from django.test import TestCase

# Create your tests here.
import random

from django.core.cache import cache

def test():
        send_mail('Subject here', 'Here is the message.', 'toolsdesu@gmail.com', ['st0963105799@gmail.com'], fail_silently=False)