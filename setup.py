# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_desc = '''
This package contains agp implementation, usable as standalone or as an openaps
plugin.

'''

requires = ['openaps>=0.0.0', 'scipy', 'numpy']

setup(
    name='openapscontrib.agp',
    version='0.0.0',
    url='http://github.com/bewest/openaps-agp',
    download_url='http://pypi.python.org/pypi/openaps-agp',
    license='BSD',
    author='Ben West',
    author_email='bewest+openaps@gmail.com',
    description='openaps agp plugin',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['openapscontrib'],
)
