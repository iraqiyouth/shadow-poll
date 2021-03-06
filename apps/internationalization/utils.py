#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

import re
from internationalization.models import Language, Translation

DEFAULT_LANGUAGE = "en"

def get_language_from_message(message):
    """ customize this function depending on the 
    default i18n behaviour your app expects
    """
    if hasattr(message,'language'):
        return message.language
    return get_language_from_connection(message.persistant_connection)

def get_language_from_connection(connection):
    """ customize this function depending on the 
    default i18n behaviour your app expects
    """
    if connection.reporter:
        if connection.reporter.language:
            return connection.reporter.language
    return DEFAULT_LANGUAGE 

def get_language_from_code(language_code):
    languages = Language.objects.all()
    for language in languages:
        if re.match(language.pattern.regex, language_code, re.IGNORECASE):
            return language
    if language_code == DEFAULT_LANGUAGE:
        # so we don't infinite loop
        return None
    return get_language_from_code(DEFAULT_LANGUAGE)

def get_translation(string, language_code):
    try:
        language = Language.objects.get(code=language_code)
    except Language.DoesNotExist, ex:
        pass
    else:
        try:
            return Translation.objects.get(language=language, code=string).translation
        except Translation.DoesNotExist, ex:
            # hopefully the default passed in string will work
            pass
    return string

