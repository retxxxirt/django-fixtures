import setuptools
from distutils.core import setup

setup(
    name='django-fixtures-rx',
    packages=['django_fixtures'],
    version='0.2.3',
    license='MIT',
    description='Advanced django fixtures.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='retxxxirt',
    author_email='retxxirt@gmail.com',
    url='https://github.com/retxxxirt/django-fixtures',
    keywords=['django', 'django fixtures', 'django-fixtures', 'fixtures', 'tests', 'unittests'],
    install_requires=['wheel'],
    package_data={'django_fixtures': ['management/commands/*.py']}
)
