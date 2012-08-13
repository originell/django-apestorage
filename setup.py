from setuptools import setup
from setuptools import find_packages


setup(
    name='django-apestorage',
    version='1.0.0',
    url='https://github.com/originell/django-apestorage',
    author='Luis Nell',
    author_email='cooperate@originell.org',
    packages=find_packages(),
    platforms='any',
    description=('Django Storage Engine which returns images of apes if '
                 'files could not be found.'),
    long_description=open('README.rst').read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Multimedia :: Graphics",
    ],
)
