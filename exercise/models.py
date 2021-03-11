from django.db import models

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
    view_link = models.CharField(max_length=500, null=True,blank=True)

    class Meta:
        ordering = ['body_part_primary','name']

    def __str__(self):
        return self.name

class ExerciseTracker(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(null=True, blank=True)
    repetitions = models.PositiveIntegerField(default=1)
    weight = models.PositiveIntegerField(null=True, blank=True)
    view_link = models.CharField(max_length=500, null=True,blank=True)
    duration = models.PositiveIntegerField(null=True, blank=True)


    class Meta:
        ordering = ['time','exercise']

    def __str__(self):
        return f'{self.exercise}, {self.time}'