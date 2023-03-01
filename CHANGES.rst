Changes
=======

1.0 (2023-03-01)
----------------

Breaking changes:

- Drop support for Python 2.7, 3.5, 3.6.

New features:

- Add support for Python 3.9, 3.10, 3.11.


0.4.1 (2020-11-12)
------------------

Bug fixes:

- zc.buildout is not an install dependency, only used in testing.

0.4.0 (2020-04-21)
------------------

Breaking changes:

- Drop support for Python 3.4.

New features:

- When environment variable ``Z3C_AUTOINCLUDE_DEBUG`` is set,
  log which packages are being automatically included.
  Do this in a form that you can copy to a ``configure.zcml`` file.

- Add support for Python 3.8.


0.3.9 (2019-03-02)
------------------

Bug fixes:

- Catch and ignore AttributeError for ``module.__file__``.
  Fixes `issue 6 <https://github.com/zopefoundation/z3c.autoinclude/issues/6>`_.
  [maurits]


0.3.8 (2018-11-04)
------------------

New features:

- Add support for Python 3.6 and 3.7.

Bug fixes:

- Fix the ``includePlugins`` directive to read filenames
  as native strings in Python 3.


0.3.7 (2016-08-24)
------------------

- Add support for Python 3.4, Python 3.5 and PyPy.

- When choosing between multiple (equivalent) packages that offer the
  same namespace and there are no namespace-only packages, choose
  either the one whose project name matches the namespace (if there
  are no dots in the namespace), or the first when sorted by project
  name. Previously, the first in the list generated from the
  combination of iterating ``sys.path`` and asking ``pkg_resources``
  for distributions was picked. This should increase test
  repeatability but is not expected to be otherwise noticeable. See
  `PR 3 <https://github.com/zopefoundation/z3c.autoinclude/pull/3>`_
  for discussion.

0.3.6 (2016-01-29)
------------------

- Standardize namespace __init__.

- Fix broken tests.


0.3.5 (2013-09-12)
------------------

* If a module cannot be resolved, but raises ``ImportError``, log a
  warn and continue. This fixes an issue where the determining the
  includable packages would fail due to a problem with the importation
  of one or potentially more modules. An example is the ``gobject``
  module which provides a Python binding to ``GObject``. In a recent
  API deprecation, one is no longer allowed to both import ``gi`` and
  ``gobject``.

0.3.4 (2011-03-11)
------------------

* Remove unnecessary distribution lookup in the PluginFinder.

0.3.3 (2010-05-06)
------------------

* Ignore case in tests in order to pass tests on Windows.

* Clearly specify license as ZPL (not public domain, as it was
  claiming before).

0.3.2 (2009-12-19)
------------------

* Let ``subpackageDottedNames`` always return a sorted list of package names as
  ``os.listdir`` doesn't on some platforms.

0.3.1 (2009-05-04)
------------------

* z3c.autoinclude no longer (spuriously) depends on PasteScript.

0.3 (2009-03-03)
----------------

* Allow virtual namespace packages like 'plone' to be specified for the
  package. I think this may need more thought for the dependency case.

* Allow ZCML ``includePlugins`` directive to specify a particular ZCML file to
  try to load from plugins, so that loading of meta, configure and overrides
  can be split across three ZCML files if desired. You can specify a file like:
  <includePlugins package="." file="silly.zcml" />.

* Provide a separate ``includePluginsOverrides`` directive to be used when
  loading overrides, and no longer look for 'overrides.zcml' files by default
  with ``includePlugins``.

* Removed the deprecated ``autoinclude`` and ``autoincludeOverrides``
  directives.

* `Allow autoinclusion to be disabled <http://lists.plone.org/pipermail/plone-framework-team/2009-February/005938.html>`_ by setting
  ``os.environ['Z3C_AUTOINCLUDE_PLUGINS_DISABLED']`` and
  ``os.environ['Z3C_AUTOINCLUDE_DEPENDENCIES_DISABLED']``, potentially useful for
  test runners or debugging sessions.

For context on many of these changes, see `the PLIP #247 discussion <http://lists.plone.org/pipermail/plone-framework-team/2009-January/005823.html>`_.

0.2.2 (2008-04-22)
------------------

* Gracefully catch KeyErrors in ``namespaceForDottedName``; get_metadata_lines
  will sometimes throw this for certain distribution types, apparently. In
  particular, some systems' version of Python itself will be wrapped in a
  distribution which throws this error, resulting in system-dependent
  unresumable breakage of z3c.autoinclude prior to this fix.

0.2.1 (2008-04-21)
------------------

* Fixed bug which prevented proper inclusion of packages when the base
  package's namespace has been extended by other installed packages.

* Rewrote ``distributionForPackage`` function.

* Added additional tests for ``includePlugins`` and utility functions.

* Fixed bug which made z3c.autoinclude look for ZCML in namespaces of nested
  namespace packages (eg, if there happened to -- improperly -- be an
  x/y/configure.zcml in a x.y.z package with an x.y namespace, it would have
  been included; this is incorrect.)

0.2 (2008-04-18)
----------------

* Added new directive ``includePlugins``.

* Renamed ``autoinclude`` directive to ``includeDependencies``.

* Deprecated ``autoinclude`` directive.

0.1 (2008-02-25)
----------------

* Initial public release.
