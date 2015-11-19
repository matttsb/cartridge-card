import datetime
from django import template
from mezzanine.conf import settings

register = template.Library()

@register.simple_tag()
def stripe_key():
    return settings.STRIPE_PUBLISHABLE


