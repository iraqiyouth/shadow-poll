#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8
from rapidsms.tests.scripted import TestScript
from poll.app import App
from poll.models import *
from reporters.app import App as reporter_app

class TestApp(TestScript):
    fixtures = ['poll_responses.json']
    apps = (App, reporter_app)

    testCorrectResponse = """
      98804 > ED 10 M 110010
      98804 < Thank you for voting. You selected Education.
      10000 > ED 10 J 110010
      10000 < Thank you for voting. You selected Education.
    """

    testCorrectResponse = """
      98804 > poll
      98804 < What is your biggest problem?
    """

