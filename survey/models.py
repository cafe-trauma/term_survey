from django.db import models

# Create your models here.
class Term(models.Model):
    label = models.CharField(max_length=200)
    annotation = models.TextField()
    uri = models.CharField(max_length=200)

    def __str__(self):
        return self.label

class Respondant(models.Model):
    identifier = models.CharField(max_length=200)
    additional_comments = models.TextField(blank=True)

    def __str__(self):
        return self.identifier

class Response(models.Model):
    term = models.ForeignKey('term', on_delete=models.CASCADE)
    respondant = models.ForeignKey('respondant', on_delete=models.CASCADE)
    is_good = models.BooleanField()
    proposal = models.TextField(blank=True)
    comment = models.TextField(blank=True)

    def __str__(self):
        return "{} - {} - {}".format(self.is_good, self.term, self.respondant)

class Setting(models.Model):
    terms_per_user = models.IntegerField()

    def __str__(self):
        return "Survey settings, only make a single row"
