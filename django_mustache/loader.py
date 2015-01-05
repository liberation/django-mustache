import os.path
import pystache

from django.conf import settings
from django.template import Template
from django.template import TemplateDoesNotExist
from django.utils.encoding import smart_unicode
from django.template.loaders import app_directories


# Note: cannot be a list of extensions
# because pystache.Renderer accepts only one.
MUSTACHE_FILE_EXTENSION = getattr(
    settings, 'MUSTACHE_FILE_EXTENSION', '.mustache')
MUSTACHE_TEMPLATE_DIRS = getattr(
    settings, 'MUSTACHE_TEMPLATE_DIRS',
    [os.path.join(settings.STATIC_ROOT, 'js', 'templates')])


class MustacheTemplate(Template):
    def __init__(self, source, origin=None, name='We will never know.'):
        # Note: source is parsed
        self.source = source
        self.name = name

    @property
    def nodelist(self):
        # Nice hack bro, makes it work with @inclusion_tag
        return self

    def render(self, context):
        context_dict = {}
        for d in context.dicts:  # Flatten
            context_dict.update(d)

        renderer = pystache.Renderer(
            search_dirs=MUSTACHE_TEMPLATE_DIRS,
            file_extension=MUSTACHE_FILE_EXTENSION[1:])
        return renderer.render(self.source, context_dict)


class MustacheLoader(app_directories.Loader):
    is_usable = True
    _parsed = {}  # Immutable! cache

    def parse_mustache_template(self, origin, source):
        # No cache in DEBUG mode
        if origin not in self._parsed or settings.DEBUG:
            try:
                self._parsed[origin] = pystache.parse(smart_unicode(source))
            except pystache.parser.ParsingError, e:
                # Better error
                raise pystache.parser.ParsingError(
                    "Mustache couldn't parse {0}, "
                    "reason : '{1}'.".format(origin, e))
        return self._parsed[origin]

    def load_template(self, template_name, template_dirs=None):
        dummy, extension = os.path.splitext(template_name)

        if extension == MUSTACHE_FILE_EXTENSION:
            source, origin = self.load_template_source(
                template_name, MUSTACHE_TEMPLATE_DIRS)
            try:
                parsed = self.parse_mustache_template(origin, source)
                template = MustacheTemplate(parsed, origin=origin,
                                            name=template_name)
                return template, None
            except TemplateDoesNotExist:
                return source, origin

        return super(MustacheLoader, self).load_template(
            template_name, template_dirs)
