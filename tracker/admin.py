from django.contrib import admin
from .models import IssueCategory, Issue, IssueState


# Register your models here.
class IssueAdmin(admin.ModelAdmin):
    fields = ['description', 'category', 'state', 'solver', 'created', 'finished']
    list_display = ('description', 'category', 'submitter', 'solver', 'state', 'created', 'finished')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.submitter = request.user
        obj.save()

admin.site.register(IssueCategory)
admin.site.register(Issue, IssueAdmin)
