from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'tracker'
urlpatterns = [
    url(r'^$', views.IssueListView.as_view(), name='index'),
]
