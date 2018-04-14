import io
from setuptools import setup

with io.open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name='boxing',
    version='0.1.4',
    url='https://github.com/acifani/boxing',
    license='BSD',
    author='Alessandro Cifani',
    author_email='alessandro.cifani@gmail.com',
    description='Draw boxes like never before!',
    long_description=readme,
    packages=['boxing'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha', 'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python'
    ])
