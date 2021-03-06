from django.test import TestCase

from apps.charts.models import Governorate
from apps.poll.models import Question,Color

class GovernorateTest(TestCase):
    fixtures = ['test_charts', 'functional_test_data.json']

    def fails_test_num_response(self):
        states = Governorate.objects.all()

        self.assertEquals(states[0].num_responses(), 2)
        self.assertEquals(states[1].num_responses(), 1)
        self.assertEquals(states[2].num_responses(), 2)
        self.assertEquals(states[3].num_responses(), 0)
        self.assertEquals(states[4].num_responses(), 0)

    def fails_test_style(self):
        states = Governorate.objects.all()

        self.assertEquals(states[0].style(), "s14")
        self.assertEquals(states[2].style(), "s14")
        self.assertEquals(states[9].style(), "s0")
        self.assertEquals(states[1].style(), "s7")
