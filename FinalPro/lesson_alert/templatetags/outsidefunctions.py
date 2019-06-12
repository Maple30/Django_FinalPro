from django import template
from django import views

register = template.Library()

@register.simple_tag
def lessonchange(value):
    return value

@register.simple_tag
def lessonNotadded():
    return 0