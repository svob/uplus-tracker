from django.conf.urls import url

from . import views

app_name = 'tracker'
urlpatterns = [
    url(r'^$', views.IssueListView.as_view(), name='index'),
]
