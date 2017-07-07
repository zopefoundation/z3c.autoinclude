from setuptools import find_packages
from setuptools import setup


setup(
    name='base2.plug',
    version='0.0',
    description="",
    long_description="""
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
    packages=find_packages(),
    namespace_packages=['base2'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'TestDirective',
    ],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = base2
    """,
)
