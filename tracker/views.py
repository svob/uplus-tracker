from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from datetime import timedelta

from tracker.models import Issue


@method_decorator(login_required, name='dispatch')
class IssueListView(generic.ListView):
    template_name = 'tracker/index.html'
    context_object_name = 'issues'

    def get_queryset(self):
        return Issue.objects.all().order_by('-created')

    def get_context_data(self, **kwargs):
        context = super(IssueListView, self).get_context_data(**kwargs)
        context['open'] = 0
        context['finished'] = 0
        context['avg'] = timedelta()
        for issue in context['issues']:
            if issue.finished is not None:
                issue.duration = issue.finished - issue.created
                context['finished'] += 1
                context['avg'] += issue.duration
            else:
                issue.duration = None
                context['open'] += 1
        context['min'] = min(context['issues'], key=lambda i: i.duration.total_seconds() if i.duration is not None else float('inf')).duration
        context['max'] = max(context['issues'], key=lambda i: i.duration.total_seconds() if i.duration is not None else 0).duration
        context['avg'] /= context['finished']
        return context