from django.db import models

"""3. Create 2 models, Question:text, publication date,
Choice: question - ForeignKey to Question, choice text,
QuestionAnwser: question ForeignKey to Question, choice ForeignKey to
Choice"""

class Question(models.Model):

    text = models.TextField()
    publication_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text


