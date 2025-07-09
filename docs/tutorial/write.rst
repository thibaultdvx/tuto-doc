Write documentation pages
=========================

Now that we have a functional documentation, we will fill it. As suggested in
the :ref:`introduction <documentation-overview>`, we will add ``installation``, ``getting started``, 
``user guide``, ``API Reference``, and ``contribution guide`` sections:

.. code-block:: bash

    echo "Installation\n============" > installation.rst 
    echo "Getting Started\n===============" > getting_started.rst
    mkdir -p user_guide && echo "User Guide\n==========" > user_guide/index.rst
    echo "10 minutes to NeuroPlot\n=======================" > user_guide/intro.rst
    echo "Plotting a 3D image\n===================" > user_guide/plot.rst
    echo "Making a GIF\n============" > user_guide/gif.rst
    echo "Multiple plots\n==============" > user_guide/multiple_plots.rst
    mkdir -p api && echo "API Reference\n=============" > api/index.rst
    echo "Contributing\n============" > contributing.rst

.. note::

    These commands are just here to make your life easier. Of course, you could have created the ``.rst`` files
    manually.

Have a look at your ``docs`` folder: ``.rst`` files are placed at the same level as your ``index.rst``. Besides, if you want
a page with subpages (e.g. the ``user guide`` here), you will create a folder, with an ``index.rst`` inside.

However, if you build the documentation (``make html``), you will not see any modification. The new pages are not visible
in our documentation... But they have been built: for example, the ``installation`` page is accessible at http://localhost:8888/installation.html.
This simply because we have to build a table of contents in our ``index.rst`` pages:

1. Change the content of ``index.rst`` with:

    .. code-block:: rst

        NeuroPlot
        =========

        NeuroPlot is a Python library for plotting neuroimaging data.

        .. toctree::
            :maxdepth: 1

            installation
            getting_started
            user_guide/index
            api/index

        .. toctree::
            :caption: development
            :maxdepth: 1

            contributing
            GitHub <https://github.com/aramis-lab/tuto-doc>

2. Change the content of ``user_guide/index.rst`` with:

    .. code-block:: rst

        User Guide
        ==========

        .. toctree::
            :numbered:

            intro
            plot
            multiple_plots
            gif

3. Build the documentation.

Can you see the new pages in the navigation bar?

Great, now let's talk about that weird ``.rst`` extension...

reStructuredText format
-----------------------

``rst`` stands for "reStructuredText". It is a convenient format to write documentation.
It is very similar to the simpler and well-know ``markdown``, although it is a bit more
powerful.

We won't dive into an extended presentation of ``rst`` syntax because we have a lot of
things to do today, and there are already many resources to get started with it
(e.g. have a look a this `quickstart <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_,
or `this one <https://docutils.sourceforge.io/docs/user/rst/quickstart.html>`_; and here is a 
`cheatsheet <https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.pdf>`_).

Besides, this tutorial is entirely written in ``rst``, so it will give you an overview of what you
can do with this syntax.

.. _markdown:

markdown
--------

If you are reluctant to learn a new syntax or if you think that ``markdown`` is enough for what you
want to do, you can still configure Sphinx so that it reads ``.md`` files. To do this, let's take a
look at how to :doc:`configure our documentation <configure>`.

-----

.. admonition:: If you don't manage to run the tutorial
    :class: important

    .. code-block:: bash

        git reset --hard 8cb1dc2fe427c2f43e036b8faa99da3cca9addf5