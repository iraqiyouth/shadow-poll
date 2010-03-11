from django import template
from django.conf import settings
from django.utils.translation import ugettext as _

register = template.Library()

@register.simple_tag
def get_languages():
    html = ""
    for key,value in settings.LANGUAGES:
        lang_html= "<a href=\"javascript:test('"
        lang_html += key
        lang_html +="')\">"
        lang_html += value
        lang_html += "</a>"
        lang_html += " | "
        html += lang_html
    return html[:-2]

@register.filter
def translate_number(value): 
    string=""
    for i in range(len(str(value))):
        string = string + _(str(value)[i])  
    return  string


@register.filter
def myPluralize(value):  
    if value > 1:
        if translate_number(str(value)[0]) in "1234567890":
            return  "s"
        else:
            return ""
    else:
         return ""
    