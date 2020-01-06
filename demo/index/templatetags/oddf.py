from django import template

register =template.Library()

@register.filter
def odd(x):
    return x*2