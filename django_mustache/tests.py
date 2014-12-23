from django.test import TestCase
from django.template import Library
from django.template import Template
from django.template import Context

from django_mustache.loader import MustacheTemplate


register = Library()


class MustacheLoaderTestCase(TestCase):

    def test_inclusiontag(self):
        t = Template(u"{% load test_tags %}{% foo_bar %}")
        expected = u"""Test bar."""
        self.assertEqual(expected, t.render(Context({})))

    def test_partials(self):
        t = MustacheTemplate(u"Test {{> test/just_foo}}.")
        expected = u"""Test bar."""
        r = t.render(Context({'foo': u"bar"}))
        self.assertEqual(expected, r)

    def test_view(self):
        r = self.client.get('/test/')
        expected = u"""Test bar."""
        self.assertEqual(expected, r.content)
