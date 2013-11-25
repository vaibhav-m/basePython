django-project-template
=======================

Django &amp; Buildout Project Template. You are encouraged to try it out, but right now, it is a work in progress.

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

1. Run ```python bootstrap.py```
2. Run ```bin/buildout```
3. If you are using PyDev, you would need to add tests folder
   as a source folder.
4. Run ```bin/fab -l``` for a list of common supported commands.
5. For anything custom, you can directly use the scripts in bin folder.
