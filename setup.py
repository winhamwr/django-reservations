import os
from distutils.core import setup

def find_packages(root):
    # so we don't depend on setuptools; from the Storm ORM setup.py
    packages = []
    for directory, subdirectories, files in os.walk(root):
        if '__init__.py' in files:
            packages.append(directory.replace(os.sep, '.'))
    return packages

setup(
    name = 'django-reservations',
    version = '0.1.b1',
    description = 'Reservation management for events and resources',
    author = 'Wes Winham',
    author_email = 'winhamwr@gmail.com',
    license = 'BSD',
    url = 'http://github.com/winhamwr/django-reservation',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
        ],
    packages = find_packages('reservation'),
)
