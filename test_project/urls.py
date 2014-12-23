from django.conf.urls import patterns, url

from test_project.views import TestView


urlpatterns = patterns('',
    url(r'^test/', TestView.as_view(), name="test_view"),
)
