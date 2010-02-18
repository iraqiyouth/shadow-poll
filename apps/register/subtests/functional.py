# -*- coding: utf-8 -*-
#imports for functional tests
from django.test import TestCase
from rapidsms import *
from rapidsms.connection import *
from rapidsms.tests.scripted import TestScript
from register.models import *
from reporters.models import PersistantBackend, Reporter
from register.app import App
import tree.app as tree_app
import register.app as register_app
import reporters.app as reporter_app
import internationalization.app as i18n_app

class TestRegisterScript (TestScript):
    apps = (tree_app.App, register_app.App, reporter_app.App, i18n_app.App)

    def setUp(self):
        TestScript.setUp(self)

    test_register_needs_keyword_at_the_start_of_the_message_rapidsms = """
      00919880438062 > not_keyword poll 100 1001
      00919880438062 > register poll 100 1001
      00919880438062 < Thank you, to initiate the poll sms the keyword Poll with your age and gender
      """

    error_message = "We don\u2019t understand. Correct format is register poll governorate-code district-code"
    test_incomplete_information_passed_in_the_register_message = """
      00919980131127 > register poll 0091998013112700919980131127
      00919980131127 < We don't understand. Correct format is register poll governorate-code district-code
      """
    
    test_incomplete_information_passed_in_the_register_message_2 = """
      00919980131127 > register poll 0091998013112700919980131127
      00919980131127 < We don't understand. Correct format is register poll governorate-code district-code
      """

class TestRegisterArabicScript (TestScript):
    apps = (tree_app.App, register_app.App, reporter_app.App, i18n_app.App)

    def setUp(self):
        TestScript.setUp(self)

    test_registration_message_in_arabic = u"""
        00919980131127 > تسجيل التصويت 100 1001
        00919980131127 < شكرا لك ، للشروع في استطلاع الرسائل القصيرة والتصويت مع الكلمة الرئيسية الخاصة بكالعمر والجنس 
    """
    
    arabic_error_message = u"نحن لا نفهم. بالشكل الصحيح هو تسجيل استطلاع للمحافظة حي رمز رمز"
    test_incomplete_information_passed_in_the_register_message_arabic = u"""
        00919980131127 > تسجيل التصويت 1شش شس 00 001
        00919980131127 < %(error_msg)s
    """ % {"error_msg":arabic_error_message}

