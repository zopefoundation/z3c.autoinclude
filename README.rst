Overview
========

This package adds two new ZCML directives to automatically detect
ZCML files to include: "includeDependencies" and "includePlugins".

When you want to include a Zope-based package in your application, you
have to repeat yourself in two places: you have to add the package
itself (in a setup.py, buildout, etc) and you also have to include its
ZCML with an <include> directive or a package-includes slug. Because
you have to repeat yourself, you can easily make an error where you
add a new package but forget to include its ZCML.

z3c.autoinclude lets you circumvent this error-prone process with
automatic detection and inclusion of ZCML files.

includeDependencies
-------------------

The "includeDependencies" directive searches through the dependencies
in your setup.py file (install_requires), and includes the ZCML files
in those packages that it finds. Inclusion order matches the order in
the setup.py file. You can pass a path for the package you want to
include dependencies for, but typically you pass in the current
package, as follows::

  <includeDependencies package="." />

With this directive, you no longer have to add an explicit ``<include
package=new.dependency>`` for every new dependency of your project.

Grok_ and grokproject_ use this functionality out of the box. The
grokproject command will automatically add the ``includeDependencies``
directive in the ZCML of the project it generates.  You can then stop
worrying about manual ZCML inclusion in the vast majority of cases.

includePlugins
--------------

The "includePlugins" directive uses entry points to find installed
packages that broadcast themselves as plugins to a particular base
package. You can pass a path for the package you want to include
plugins for, but typically you pass in the current package, as
follows::

  <includePlugins package="." />

To broadcast a package as a plugin to a base package called "my_base",
add the following lines to the plugin package's ``setup.py``::

  entry_points="""
  [z3c.autoinclude.plugin]
  target = my_base
  """

The Details
===========

Setup
-----

To make the z3c.autoinclude directives available for use in your
application or framework, you need to include it (in your
``meta.zcml`` for instance), like this::

  <include package="z3c.autoinclude" file="meta.zcml" />

Grok already does this for you automatically.

Disabling z3c.autoinclude
-------------------------

It is often useful to disable z3c.autoinclude's functionality for
debugging purposes or test runs.  To disable autoinclusion, set
the environment variables "Z3C_AUTOINCLUDE_DEPENDENCIES_DISABLED" and
"Z3C_AUTOINCLUDE_PLUGINS_DISABLED".

When autoinclusion is disabled, the autoinclusion directives will
issue a warning to the log and do nothing.

When environment variable "Z3C_AUTOINCLUDE_DEBUG" is set,
we log which packages are being automatically included.
We do this in a form that you can copy to a configure.zcml file.


ZCML Filenames
--------------

The includeDependencies directive automatically includes
``configure.zcml`` and ``meta.zcml`` files that live in the main
package directories. For automatic inclusion of dependencies'
overrides, there is an <includeDependenciesOverrides> directive.

In some cases, a package may use unusual names or
locations for its ZCML files. In that case you will need to modify
your package's ``configure.zcml`` and ``meta.zcml`` yourself to
include the ZCML using the manual ``include`` directive.

The includePlugins directive automatically includes ``configure.zcml``
and ``meta.zcml`` files by default, and the includePluginsOverrides
directive automatically includes ``overrides.zcml`` files by default.
But, like "<include>", these directives also have an optional "file"
parameter, so you can automatically include all ``foo.zcml`` files in
your package's plugins like this::

  <includePlugins package="." file="foo.zcml" />

The includeDependencies directives will soon offer this option as well.

.. _Grok: http://grok.zope.org

.. _grokproject: http://pypi.python.org/pypi/grokproject
