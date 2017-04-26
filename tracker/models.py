from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class IssueState(models.Model):
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.state

class IssueCategory(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = 'Issue categories'

class Issue(models.Model):
    submitter = models.ForeignKey(User, related_name='%(class)s_created')
    solver = models.ForeignKey(User, related_name='%(class)s_solved')
    description = models.CharField(max_length=500)
    state = models.ForeignKey(IssueState)
    category = models.ForeignKey(IssueCategory)
    created = models.DateTimeField(default=timezone.now)
    finished = models.DateTimeField(null=True, blank=True)
