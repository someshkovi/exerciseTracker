from django.contrib import admin

from exercise.models import ExerciseTracker, Exercise, BodyPart
# Register your models here.

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['name', 'body_part_primary']
    list_filter = ['name', 'body_part_primary']

admin.site.register(BodyPart)


class FilterUserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.trainee = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(FilterUserAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(trainee=request.user)

    def has_change_permission(self, request, obj=None):
        if not obj:
            return True
        return obj.trainee == request.user

@admin.register(ExerciseTracker)
class ExerciseTrackerAdmin(FilterUserAdmin):
    list_editable = ['count', 'repetitions', 'weight']
    list_display = ['time', 'exercise', 'count', 'repetitions', 'weight']
    list_filter = ['time', 'exercise']
    exclude = ['trainee',]

    def save_model(self,request, obj, form, change):
        if not obj.pk:
            obj.trainee = request.user
        obj.save()

    def queryset(self, request):
        """
        Filtering the objects dispalyed in the change_list
        to only display those for current signed in user
        """

        qs = super(ExerciseTrackerAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(trainee=request.user)

admin.site.site_header = 'Exercise Tracker'
admin.site.site_title = 'Exercise Tracker'
