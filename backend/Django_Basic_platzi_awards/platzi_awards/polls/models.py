from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    """Question class for poll app"""
    # id: Django generate an id automatically so we don't need create
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        """Modify str method"""
        return self.question_text

    def was_published_recently(self):
        """Now if a question was published at 1 day max"""
        return self.pub_date >= timezone.now - datetime.timedelta(days=1)

class Choice(models.Model):
    """Choiches class"""
    #id: again, Django give us and automatic ID
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """Modify str method"""
        return self.choice_text
