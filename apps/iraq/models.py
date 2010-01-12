from django.db import models

GENDER = ( ('M', 'Male'), ('F', 'Female') )

class Question(models.Model):
    question = models.CharField(null=False, max_length=200)

    def __unicode__(self):
        return self.question

class Choice(models.Model):
    choice = models.CharField(null=False, max_length=100)
    short_code = models.CharField(null=False, max_length=2)
    question = models.ForeignKey('Question')

    def __unicode__(self):
        return self.choice

class PollResponse(models.Model):
    issue = models.ForeignKey('Choice')
    age = models.IntegerField()
    location = models.IntegerField(null = True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER)
    mobile_number = models.IntegerField()
    latitude = models.DecimalField(max_digits=8, decimal_places=6, null = True)
    longitude = models.DecimalField(max_digits=8, decimal_places=6, null = True)

    def generate_response(self, text):
        try :
            foo = text.split(" ")
            self.issue = Choice.objects.get(short_code=foo[0])
            self.age = foo[1]
            self.gender = foo[2]
            try :
                self.location = foo[3]
            except IndexError:
                pass
            self.save()
        except :
            return "Sorry, we did not understand your response. Please re-send as - issue age gender area"
        return "Thank you for voting. You selected %s as your number one issue." % (self.issue)
