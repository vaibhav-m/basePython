Django &amp; Buildout Project Template
==============================================

A Django &amp; Project Template to integrate Django, Buildout, Pylint, JSHint, Sphinx etc. 
Its a work in progress and expected to evolve further. The motivation to do this came from
using Maven for Java projects.

### Project Setup
1. ```git clone``` this repository.
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

### Project Dependencies
Runtime project dependencies should be added in ```setup.py```. That is the standard python way. However, ```buildout.cfg``` 
also has multiple parts and dependencies installed using ```recipe = zc.recipe.egg```. Build or Test only dependencies can 
be add here.


### Faster Builds

Keep the following setting in default buildout config at ```~/.buildout/default.cfg```.
Its a common buildout tip to keep download times low and builds faster.

```python
[buildout]
eggs-directory = <HOME-DIR>/.buildout/eggs
download-cache = <HOME-DIR>/.buildout/dlcache
```

### Project Structure & Customizations

```buildout.cfg``` is the config to install eggs and generate scripts in bin folder.<br/>
```fabfile.py``` contains fabric tasks. You can modify it to add your own.<br/>
```etc/lint.rc``` contains pylint configuration.<br/>
```etc/jshint.json``` contains jshint settings.<br/>
```tests``` contains tests organized in unit, integration and ui packages.

Each of the above can be modified and customized as much as you want. If you implement something generally 
useful, please contribute it back.


### TODOs
Contributions and ideas are welcome. These are some ideas we would like to implement.

1. ```test_js``` target to run javascript tests using a node js framework like mocha etc.
2. ```django-pipeline``` for static assets management.
3. ```build``` for jenkins build and package
4. ```incr``` for linting or testing incremental changes e.g. modified files only.
5. more ...
