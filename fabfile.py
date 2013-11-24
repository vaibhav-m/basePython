from fabric.api import task, run, local

COVERAGE_ENABLED = False
PROJECT_PACKGE = 'djprotemplate'

@task()
def docs_gen():
    '''Generates Documents. Picks sources from docs folder.'''
    local("bin/sphinxbuilder")

@task()
def runserver():
    '''Runs Django Server on port 8000'''
    local("bin/django runserver 0.0.0.0:8000")

@task()
def lint():
    '''Reports Pylint Errors & Warnings for Python files'''
    local('bin/pylint --rcfile=etc/lint.rc %s' % PROJECT_PACKGE)

@task()
def coverage():
    '''Enables Coverage. Used for test targets'''
    global COVERAGE_ENABLED
    COVERAGE_ENABLED = True


@task()
def test_all():
    '''Runs All Tests in src and tests folders'''
    options = ['--with-progressive']

    if COVERAGE_ENABLED:
        options.append('--with-coverage')
        options.append('--cover-package=%s' % PROJECT_PACKGE)

    local('bin/test test %s' % ' '.join(options))

@task()
def test_integration():
    '''Runs All Tests in tests/integration package'''
    raise Exception("Not Yet Implemented")

@task()
def test_unit():
    '''Runs All Tests in tests/unit package'''
    raise Exception("Not Yet Implemented")


