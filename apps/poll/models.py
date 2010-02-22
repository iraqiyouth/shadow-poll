from django.db import models
from apps.reporters.models import Reporter, PersistantConnection
import re
from register.models import Registration

class QuestionTree(models.Model):
    questions = []
    flow = {}

    def addQuestion(self, question):
        self.addToTheFlow(question)
        self.questions.append(question)

    def addToTheFlow(self, question):
        if len(self.questions) > 0 :  
            self.flow[self.questions[-1]] =question
        
    def next(self, question):
        return self.flow[question]


class Question(models.Model):
    text = models.TextField()
    max_choices = models.IntegerField()
    error_response = models.TextField(null=True, blank=True)

    
    def __unicode__(self):
        return "Q%s: %s" % (
            self.pk,
            self.text)
    
class Choice(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question)
    

