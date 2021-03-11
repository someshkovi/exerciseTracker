from django.contrib import admin

from exercise.models import ExerciseTracker, Exercise, BodyPart
# Register your models here.

@admin.register(ExerciseTracker)
class ExerciseTrackerAdmin(admin.ModelAdmin):
    list_display = ('time', 'exercise', 'count')
    list_filter = ('time', 'exercise')

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'body_part_primary')
    list_filter = ('name', 'body_part_primary')

admin.site.register(BodyPart)