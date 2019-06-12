import random

from django.core.management.base import BaseCommand
from django.core.cache import cache
from django.core.mail import send_mail
class Command(BaseCommand):
    """
    自定义命令
    """
    def handle(self, *args, **options):
        send_mail('Subject here', 'Here is the message.', 'toolsdesu@gmail.com', ['st0963105799@gmail.com'], fail_silently=False)