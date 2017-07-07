from setuptools import find_packages
from setuptools import setup


setup(
    name='enolp.ppa.foo',
    version='0.1',
    description="",
    long_description="""
""",
    # Get more strings from
    # http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Zope3",
        "Programming Language :: Python",
    ],
    keywords='',
    author='',
    author_email='',
    url='',
    license="''",
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['enolp', 'enolp.ppa'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'TestDirective',
        # -*- Extra requirements: -*-
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,
)
