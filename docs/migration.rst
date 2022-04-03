.. Copyright (c) 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022 Python Software Foundation; All Rights Reserved
..
.. SPDX-License-Identifier: PSF-2.0

.. _migration:

Migrating from older APIs
=========================

This section has information on migrating from older APIs.

The ``pkg_resources`` resource API
----------------------------------

Basic resource access
~~~~~~~~~~~~~~~~~~~~~

``resource_exists(package, resource_name)``
   ``finder(package).find(resource_name) is not None``

``resource_stream(package, resource_name)``
   ``finder(package).find(resource_name).as_stream()``

``resource_string(package, resource_name)``
   ``finder(package).find(resource_name).bytes``

``resource_isdir(package, resource_name)``
   ``finder(package).find(resource_name).is_container``

``resource_listdir(package, resource_name)``
   ``finder(package).find(resource_name).resources``

Resource extraction
~~~~~~~~~~~~~~~~~~~

``resource_filename(package, resource_name)``
   ``finder(package).find(resource_name).file_path``

``set_extraction_path(extraction_path)``
   This has no direct analogue, but you can achieve equivalent results by
   doing something like the following::

    from distlib import resources

    resources.cache = resources.Cache(extraction_path)

   before accessing the ``file_path`` property of any :class:`Resource`.
   Note that if you have accessed the ``file_path`` property for a resource
   *before* doing this, the cache may already have extracted files.

``cleanup_resources(force=False)``
   This is not actually implemented in ``pkg_resources`` -- it's a no-op.
   You could achieve the analogous result using::

    from distlib import resources

    not_removed = resources.cache.clear()

Provider interface
~~~~~~~~~~~~~~~~~~

You can provide an ``XXXResourceFinder`` class which finds resources in custom
storage containers, and works like ``ResourceFinder``. Although it shouldn't
be necessary, you could also return a subclass of :class:`Resource` from your
finders, to deal with custom requirements which aren't catered for.

``get_cache_path(archive_name, names=())``
   There's no analogue for this, as you shouldn't need to care about whether
   particular resources are implemented in archives or not. If you need this
   API, please give feedback with more information about your use cases.

``extraction_error()``
   There's no analogue for this. The :meth:`Cache.get` method, which writes
   a resource's bytes to a file in the cache, will raise any exception caused
   by underlying I/O. If you need to handle this in the cache layer, you can
   subclass :class:`Cache` and override :meth:`get`. If that doesn't work for
   you, please give feedback with more information about your use cases.

``postprocess(tempname, filename)``
   There's no analogue for this. The :meth:`Cache.get` method, which writes
   a resource's bytes to a file in the cache, can be overridden to perform any
   custom post-processing. If that doesn't work for you, please give feedback
   with more information about your use cases.

The ``pkg_resources`` entry point API
-------------------------------------

Entry points in ``pkg_resources`` are equivalent to per-distribution exports
dictionary (see :ref:`dist-exports`). The keys to the dictionary are just names
in a hierarchical namespace delineated with periods (like Python packages).
These keys are called *groups* in ``pkg_resources`` documentation, though that
term is a little ambiguous. In Eclipse, for example, they are called *extension
point IDs*, which is a little closer to the intended usage, but a bit of a
mouthful. In ``distlib``, we'll use the term ``category`` or ``export category``.

In ``distlib``, the implementation of exports is slightly different from
entry points of ``pkg_resources``. A :class:`Distribution` instance has an
``exports`` attribute, which is a dictionary keyed by category and whose values
are dictionaries that map names to :class:`ExportEntry` instances.

Below are the ``pkg_resources`` functions and how to achieve the equivalent
in ``distlib``. In cases where the ``pkg_resources`` functions take distribution
names, in ``distlib`` you get the corresponding :class:`Distribution` instance,
using::

    dist = dist_path.get_distribution(distname)

and then ask that instance (or the ``dist_path`` instance) for the things you
need.

``load_entry_point(distname, groupname, name)``
   ``dist.exports[groupname][name].value``

``get_entry_info(distname, groupname, name)``
   ``dist.exports[groupname][name]``

``get_entry_map(distname, groupname=None)``
   ``dist.exports`` or ``dist.exports[groupname]``

``iter_entry_points(groupname, name=None)``
   ``dist_path.get_exported_entries(groupname, name=None)``
