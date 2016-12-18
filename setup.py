from setuptools import setup
from os import path
from codecs import open

root_dir = path.abspath(path.dirname(__file__))

with open( path.join( root_dir, 'README.rst' ), encoding = 'utf-8' ) as f:
    long_description = f.read()

setup(
    name='pyman',
    version='0.1.1a3',
    url='https://github.com/MarkLark/pyman',
    license='MIT',
    author='Mark Pittaway',
    author_email='mark.pittaway@mlit.net.au',
    description='A CLI for managing python projects',
    long_description=long_description,
    packages=['pyman'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: User Interfaces',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: POSIX :: Linux'
    ]
)
