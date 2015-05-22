from setuptools import setup, find_packages

setup(
    name="basePython",
    version="0.0.1",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['setuptools', 'Django', 'newrelic'],
)
