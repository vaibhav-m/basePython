from setuptools import setup, find_packages

setup(
    name="django-project-template",
    version="0.0.1",
    url='http://github.com/hashedin/django-project-template',
    license='BSD',
    description="A Common Buildout Django Template",
    author='Anshuman Singh',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['setuptools', 'Django', 'Fabric'],
)
