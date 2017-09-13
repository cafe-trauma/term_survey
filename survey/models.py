from django.db import models

# Create your models here.
class Term(models.Model):
    label = models.CharField(max_length=200)
    annotation = models.TextField()
    uri = models.CharField(max_length=200)

    def __str__(self):
        return self.label

class Respondant(models.Model):
    additional_comments = models.TextField(blank=True)

    def __str__(self):
        return str(self.id)

class Response(models.Model):
    term = models.ForeignKey('term', on_delete=models.CASCADE)
    respondant = models.ForeignKey('respondant', on_delete=models.CASCADE)
    is_good = models.NullBooleanField(blank=True, null=True, default=None)
    proposal = models.TextField(blank=True)
    comment = models.TextField(blank=True)

    class Meta:
        unique_together = ('term', 'respondant')

    def __str__(self):
        return "{} - {} - {}".format(self.is_good, self.term, self.respondant)

class Setting(models.Model):
    terms_per_user = models.IntegerField()
    logo = models.URLField(blank=True)
    welcome_message = models.TextField(blank=True)
    header = models.CharField(max_length=50)

    def __str__(self):
        return "Survey settings, only make a single row"
