from setuptools import find_packages
from setuptools import setup


setup(
    name='SRCPackage',
    version='0.0',
    description="",
    long_description="""\
""",
    # Get strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[],
    keywords='',
    author='',
    author_email='',
    url='',
    license='',
    package_data={'': ['*.zcml', ]},
    packages=find_packages('src', exclude=['ez_setup', 'examples', 'tests']),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'BCPackage',
        'z3c.autoinclude',
        'TestDirective',
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,
)
