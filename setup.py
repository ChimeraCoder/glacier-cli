from distutils.core import setup

setup(
    name='glacier-cli',
    version='0.0.1',
    author='Aditya Mukerjee',
    author_email='dev@chimeracoder.net',
    packages=[], #Later on, glacier.py should probably be factored out into 'glacier', etc.
    url='https://github.com/ChimeraCoder/glacier-cli',
    license='MIT',
    description='A sysadmin-friendly command line interface to Amazon Glacier',
    long_description=open('README').read(),
    install_requires=['iso8601', 'sqlalchemy'],
)
