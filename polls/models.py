from django.db import models

""" FARI when we run 'python manage generatemigration <nameofthismodule> it will generate a Migration class (which inherits from django.db.migrations.Migration) in the migration folder and set the table names and fields and relationships and such
it does stuff like 'migrations.CreateModel( name = 'Question')
The name in the database ends up being pools_question thoughj
"""

# Create your models here.


class Question(models.Model):
    # id field is created automatically for all models and it's auto increment
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        # it's something that will be displayed by the admin tool so instead
        # of getting that weird object name/address stuff we give a name
        return self.question_text


class Choice(models.Model):
    question_text = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
