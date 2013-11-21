from fabric.api import task, run

@task()
def docs_gen():
    run("bin/sphinxbuilder")

def docs_package():
    run("echo Packaging Docs")

def django_start(project_name="defaultproject"):
    run("bin/django-admin.py startproject --pythonpath=./src %s src" % project_name)
