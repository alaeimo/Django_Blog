import hashlib
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

# return only the URL of the gravatar
# TEMPLATE USE:  {{ username|gravatar_url:150 }}
@register.filter
def gravatar_url(username,size=40):
    random_string = "This is a random string &%#$@#1654965316549+8$@$%^@^"
    username_hash = hashlib.md5((username.lower()+random_string).encode('utf-8')).hexdigest()
    return f"https://www.gravatar.com/avatar/{username_hash}?s={size}&d=identicon"