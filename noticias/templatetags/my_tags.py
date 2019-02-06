from django import template
register = template.Library()


@register.filter(name='videocut')
def get_video_link(value):
    url = value.split('/watch?v=')[1]
    return url


@register.filter(name='urlcut')
def get_video_link(value):
    url = value.split('/watch?v=')[1]
    return value.replace(value, url)
