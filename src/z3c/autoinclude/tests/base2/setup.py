from setuptools import find_packages
from setuptools import setup


setup(
    name='base2',
    version='0.0',
    description="",
    long_description="""\
    """,
    classifiers=[
        # Get strings from
        # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='',
    author='',
    author_email='',
    url='',
    license='',
    package_data={'': ['*.zcml', ]},
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['base2'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'z3c.autoinclude',
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,
)
