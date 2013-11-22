from fabric.api import task, run, local

@task()
def docs_gen():
    '''Generates Documents'''
    local("bin/sphinxbuilder")

@task()
def runserver():
    '''Runs Django Server'''
    local("bin/django runserver")

@task()
def lint():
    '''Runs Test'''
    local('bin/pylint --rcfile=etc/lint.rc --disable=RP0101 djprotemplate')
