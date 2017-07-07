from setuptools import find_packages
from setuptools import setup


setup(
    name='b.c',
    version='0.1',
    description="",
    long_description="""\
    """,
    classifiers=[
        # Get more strings from
        # http://www.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='',
    author='',
    author_email='',
    url='',
    license='',
    package_data={'': ['*.zcml', ]},
    packages=find_packages(),
    namespace_packages=['b'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'TestDirective',
        'f.g',
        # -*- Extra requirements: -*-
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,
)
