from django.utils.safestring import mark_safe
from django.template import Library




register = Library()


@register.filter(is_safe=True)
def sub(a,b):
    return mark_safe(a-b)