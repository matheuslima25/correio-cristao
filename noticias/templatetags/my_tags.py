import re
from django import template
register = template.Library()


@register.filter(name='urlcut')
def get_video_link(value):
    url = value.split('/watch?v=')[1]
    return value.replace(value, url)


@register.filter(name='youtube_embed_url')
# converts youtube URL into embed HTML
# value is url
def youtube_embed_url(value):
    match = re.search(r'^(http|https)\:\/\/www\.youtube\.com\/watch\?v\=(\w*)(\&(.*))?$', value)
    if match:
        embed_url = 'http://www.youtube.com/embed/%s' %(match.group(2))
        res = "<iframe id=\"ytVideo\" width=\"100%%\" height=\"415\" src=\"%s\"?version=3?enablejsapi=1 frameborder=\"0\" allow=\"accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe>" %(embed_url)
        return res
    return ''


youtube_embed_url.is_safe = True
