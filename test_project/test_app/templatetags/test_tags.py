from django.template import Library

register = Library()


@register.inclusion_tag('test/foo_bar.mustache')
def foo_bar():
    return {'foo': u"bar"}
