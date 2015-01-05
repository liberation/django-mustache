Lightweight [Django](https://www.djangoproject.com/) template loader for the [Mustache](http://mustache.github.io/) templating language, using [pystache](https://github.com/defunkt/pystache).  
This only handles the server side rendering, but the main goal is obviously to remain dry by avoiding duplicating templates when rendering something client side.


Install
=======

```shell
pip install git+ssh://git@github.com/liberation/django-mustache.git
```
**Note**: no pypy package yet  

Replace ```django.template.loaders.app_directories.Loader``` with ```django_mustache.loader.MustacheLoader``` in ```settings.TEMPLATE_LOADERS```.  

Because we are expecting the templates to be served through the 'static' channel, there is a different setting for ```MUSTACHE_TEMPLATE_DIRS```, it avoids the cluttering of ```TEMPLATE_DIRS``` and is a bit more efficient. If you don't need this, you can simply do : ```MUSTACHE_TEMPLATE_DIRS = TEMPLATE_DIRS```.

Note: **NO NEED** to add ```django_mustache``` to ```settings.INSTALLED_APPS```, unless you want to run the tests.  


Settings
========

* **MUSTACHE_TEMPLATE_DIRS**:  
  Defaults to ```[os.path.join(settings.STATIC_ROOT, 'js', 'templates')]```  

* **MUSTACHE_FILE_EXTENSION**:  
  Defaults to ```'.mustache'```  
  Will only use Mustache for templates files with one this extension, fallback on regular django templating language.


Tests
=====

Add django_mustache to settings.INSTALLED_APPS.

```shell
$ cd test_project
$ virtualenv env1.7
$ . env1.7/bin/activate
$ pip install "django>=1.7, <1.8"  # install the highest 1.7 version
$ python manage.py test django_mustache
```

**compatibility**: Django **1.4** to **1.7**