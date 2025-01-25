from django.db import models

DAY_CHOICES = (
    ("M", 'Monday'),
    ("Tu", 'Tuesday'),
    ("W", 'Wednesday'),
    ("Th", 'Thursday'),
    ("F", 'Friday'),
    ("Sa", 'Saturday'),
    ("Su", 'Sunday'),
)

class Day(models.Model):
    name = models.CharField(choices=DAY_CHOICES, unique=True, max_length=2)

class Event(models.Model):
    name = models.CharField(max_length=180)
    start_time = models.DateTimeField()
    duration = models.DurationField()
    repeating = models.BooleanField(default=False)
    repeating_days = models.ManyToManyField(Day, blank=True)