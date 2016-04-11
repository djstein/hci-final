from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Climb(models.Model):

    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    ELEVEN= 11
    TWELVE= 12
    THIRTEEN = 13
    FOURTEEN = 14


    DIFFICULTY = (
        (FIVE, '5'),
        (SIX, '6'),
        (SEVEN, '7'),
        (EIGHT, '8'),
        (NINE, '9'),
        (TEN, '10'),
        (ELEVEN, '11'),
        (TWELVE, '12'),
        (THIRTEEN, '13'),
        (FOURTEEN, '14'),
    )

    A = 'a'
    B = 'b'
    C = 'c'
    D = 'd'

    GRADE = (
        (A, 'a'),
        (B, 'b'),
        (C, 'c'),
        (D, 'd'),
    )

    name = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='wsgi/static/img', blank=True)
    difficulty = models.IntegerField(choices=DIFFICULTY, default=FIVE)
    grade = models.CharField(max_length=1, choices=GRADE, default=A)
    notes = models.TextField(default="")

class Attempt(models.Model):
    climb = models.ForeignKey(Climb)
    date = models.DateField()
    attempt_notes = models.TextField(default="")
