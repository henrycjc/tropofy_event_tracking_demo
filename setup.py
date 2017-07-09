from setuptools import setup, find_packages

requires = [
    'tropofy',
]

setup(
    name='tropofy-event-tracking-demo',
    version='1.0',
    description='A simple attraction popularity tracking system for an event (demo).',
    author='Henry Chladil <henry.ponco@gmail.com>',
    url='http://www.tropofy.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
)
