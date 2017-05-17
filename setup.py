#!/usr/bin/env python


from setuptools import setup

setup(
    name='pyextract',
    version='1.0.0',
    install_requires=[],
    author='Spatial Current Developers',
    author_email='opensource@spatialcurrent.io',
    license='BSD License',
    url='https://github.com/spatialcurrent/pyextract/',
    keywords='python',
    description='A nullsafe-like function for Python that can be used to extract data from dicts, lists, etc.',
    long_description=open('README.rst').read(),
    download_url="https://github.com/spatialcurrent/pyextract/zipball/master",
    packages=["pyextract"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
