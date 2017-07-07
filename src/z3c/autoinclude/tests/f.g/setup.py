from setuptools import find_packages
from setuptools import setup


version = '0.0'

setup(name='f.g',
      version=version,
      description="",
      long_description="""\
""",
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='',
      author_email='',
      url='',
      license='GPL',
      package_data = {'': ['*.zcml',]},
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      namespace_packages=['F'],
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
