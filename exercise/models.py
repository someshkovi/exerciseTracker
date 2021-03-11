from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
# from embed_video.fields import EmbedVideoField

# Create your models here.
class BodyPart(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(max_length=200)
    body_part_primary = models.ForeignKey(BodyPart, on_delete=models.CASCADE)
    other_body_parts = models.CharField(max_length=200, null=True,blank=True)
    view_link = models.URLField(max_length=500, null=True,blank=True)
    # video = EmbedVideoField(null=True,blank=True)

    class Meta:
        ordering = ['body_part_primary','name']

    def __str__(self):
        return self.name

class ExerciseTracker(models.Model):
    time = models.DateField(auto_now_add=True)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    count = models.PositiveSmallIntegerField(null=True, blank=True)
    repetitions = models.PositiveSmallIntegerField(default=1)
    weight = models.DecimalField(max_digits=4,
                                    decimal_places=2,
                                    validators=[MinValueValidator(Decimal('0.01'))],
                                    null=True,
                                    blank=True)
    view_link = models.URLField(max_length=500, null=True,blank=True)
    duration = models.DecimalField(max_digits=4,
                                    decimal_places=2,
                                    validators=[MinValueValidator(Decimal('0.01'))],
                                    null=True,
                                    blank=True)

    class Meta:
        ordering = ['time','exercise']

    def __str__(self):
        return f'{self.exercise}, {self.time}'