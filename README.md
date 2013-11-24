django-project-template
=======================

Django &amp; Buildout Project Template

## Buildout Setup
I keep the following setting in my default buildout config. Keeps
builds fast.

```python
# Create this file ~/.buildout/default.cfg
[buildout]
eggs-directory = <HOME-DIR>/.buildout/eggs
download-cache = <HOME-DIR>/.buildout/dlcache
```

## Setup Steps

#. Run ```python bootstrap.py```
#. Run ```bin/buildout```
#. If you are using PyDev, you would need to add tests folder
   as a source folder.
#. Run bin/fab -l for a list of common supported commands.
#. For anything custom, you can directly use the scripts in bin folder.
