Django &amp; Buildout Project Template
==============================================

A Django &amp; Project Template to integrate Django, Buildout, Pylint, JSHint, Sphinx etc. 
Its a work in progress and expected to evolve further. The motivation to do this came from
using Maven for Java projects.

### Project Setup
2. Run ```python bootstrap.py```
3. Run ```bin/buildout```
5. Run ```bin/fab -l``` for a list of common supported commands.


### Supported Commands

```
    coverage          Enables Coverage. Used for test targets
    docs_gen          Generates Documents. Picks sources from docs folder.
    lint_js           Reports Pylint Errors & Warnings for Python files
    lint_py           Reports Pylint Errors & Warnings for Python files
    runserver         Runs Django Server on port 8000
    test_all          Runs All Tests in src and tests folders
    test_integration  Runs All Tests in tests/integration package
    test_unit         Runs All Tests in tests/unit package
    uml_gen           Generates Package Dependency Diagrams. Assumes Graphviz.
```

**Note**: Whenever running a command **always** prefix it with bin or else your system wide installation would be used.
**Note**: For running tests along with coverage, use ```bin/fab coverage test_unit``` etc.

### Faster Builds

Keep the following setting in default buildout config at ```~/.buildout/default.cfg```.
Its a common buildout tip to keep download times low and builds faster.

```python
[buildout]
eggs-directory = <HOME-DIR>/.buildout/eggs
download-cache = <HOME-DIR>/.buildout/dlcache
```

### Project Structure & Customizations

```buildout.cfg``` is the config to install eggs and generate scripts in bin folder.
```fabfile.py``` contains fabric tasks. You can modify it to add your own.
```etc/lint.rc``` contains pylint configuration.
```etc/jshint.json``` contains jshint settings.
```tests``` contains tests organized in unit, integration and ui packages.


### TODOs
Contributions and ideas are welcome. These are some ideas we would like to implement.

1. ```test_js``` target to run javascript tests using a node js framework like mocha etc.
2. ```django-pipeline``` for static assets management.
3. ```build``` for jenkins build and package
4. ```incr``` for linting or testing incremental changes e.g. modified files only.
5. more ...
