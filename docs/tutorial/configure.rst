Configure your Sphinx documentation
===================================

Ok, now we want to customize/configure our Sphinx documentation.
The ``docs/conf.py`` file play a crucial role. Have a look at it!

It is a Python file, so it can definitely contain Python logic. However
it is mostly use to define some variables. For example, the theme is
associated with the variable ``html_theme``. Let's change its value to
see what happens.

Change the theme
----------------

We will try to substitute the basic theme with a prettier one. We choose the `furo theme <https://github.com/pradyunsg/furo>`_.

First, we need to install it:

.. code-block:: bash

    poetry add furo --group docs

Then, in ``docs/conf.py``, change ``html_theme`` to ``html_theme = "furo"``.

Finally, build the documentation! (``make html``).

It looks better, doesn't it?

Change the title
----------------

The current title is a bit long. Let's put only ``NeuroPlot`` as title.

In ``docs/conf.py``, add ``html_title = "NeuroPlot"``.

Add a logo
----------

We still miss a logo! There's no official ``NeuroPlot`` logo yet, so let's use ARAMIS logo.

We can download it 
`here <https://owncloud.icm-institute.org/index.php/apps/files/?dir=/ARAMISLAB-Shared/Logo/Sources/logos_png&fileid=39809112#/ARAMISLAB-Shared/Logo/Sources/logos_png/logo_ARAMISLAB_rvb.png>`_.

And then put it in ``docs/_static/logos``. As you have guess, the ``_static`` folder is where you
will put all the images or other resources that you want your website to use.

Finally, in ``docs/conf.py``, add the variable ``html_logo = "_static/logos/logo_ARAMISLAB_rvb.png"``.

As usual, build your documentation to see the result!

Improve design
--------------

I don't know about you, but I'm not totally satisfied with the home page. I would like to
improve its design. To do that, we will use the `sphinx-design <https://sphinx-design.readthedocs.io/en/latest/>`_
extension.

First, we need to install it:

.. code-block:: bash

    poetry add sphinx-design --group docs

Then, we will tell Sphinx to use it. In ``docs/conf.py``, change ``extensions`` to ``extensions = ["sphinx_design"]``.

Now, we can use its features. For example, change your ``docs/index.rst`` to:

.. dropdown:: ``docs/index.rst``

    .. code-block:: rst

        NeuroPlot
        =========

        NeuroPlot is a Python library for plotting neuroimaging data.

        .. grid::

            .. grid-item-card:: Installation
                :link: installation
                :link-type: doc
                :columns: 12 12 6 6
                :class-card: sd-shadow-md
                :class-title: sd-text-primary
                :margin: 2 2 0 0

                Install NeuroPlot

            .. grid-item-card:: Getting Started
                :link: getting_started
                :link-type: doc
                :columns: 12 12 6 6
                :class-card: sd-shadow-md
                :class-title: sd-text-primary
                :margin: 2 2 0 0

                Overview of NeuroPlot's main features

            .. grid-item-card:: User Guide
                :link: user_guide/index
                :link-type: doc
                :columns: 12 12 6 6
                :class-card: sd-shadow-md
                :class-title: sd-text-primary
                :margin: 2 2 0 0

                More details on NeuroPlot's features

            .. grid-item-card:: API Reference
                :link: api/index
                :link-type: doc
                :columns: 12 12 6 6
                :class-card: sd-shadow-md
                :class-title: sd-text-primary
                :margin: 2 2 0 0

                Code with NeuroPlot

        .. toctree::
            :maxdepth: 1
            :hidden:

            installation
            getting_started
            user_guide/index
            api/index

        .. toctree::
            :caption: development
            :maxdepth: 1
            :hidden:

            contributing
            GitHub <https://github.com/aramis-lab/tuto-doc>

Other improvements
------------------

I think you're beginning to understand how it works: to change settings in our
documentation, we change/add variable in ``docs/conf.py``. Sometimes, we also need to
install extensions.

To make sure you're completely comfortable with Sphinx settings, let's take as examples
two other features that we would like to implement:

- in our ``Installation`` page, we will probably have commands that the user
  would like to copy easily, so we would like a copy button;
- as mentioned :ref:`earlier <markdown>`, we would like Sphinx to be able to read ``markdown``
  files.

To implement these features, we will use respectively 
`sphinx-copybutton <https://sphinx-copybutton.readthedocs.io/en/latest/>`_ and
`myst-parser <https://myst-parser.readthedocs.io/en/v0.16.1/index.html>`_:

1. Install the extensions:

.. code-block:: bash

    poetry add sphinx-copybutton --group docs
    poetry add myst-parser --group docs

2. Add the extensions in ``docs/conf.py``:

.. code-block:: python

    extensions = [
        "sphinx_design",
        "sphinx_copybutton",
        "myst_parser",
    ]

3. Test the functionalities:

- Change ``docs/installation.rst`` to:

.. code-block:: rst

    Installation
    ============

    .. code-block:: bash

        pip install neuroplot

- Replace ``docs/contributing.rst`` with a ``docs/contributing.md``:

.. code-block:: bash

    rm contributing.rst
    echo "# Contributing" > contributing.md

Rebuild and have a look at the result in your website!

.. raw:: html

   <br><br>

I hope Sphinx configuration is clear now. Please understand that we have only mentioned
a few examples of the many features offered by Sphinx.

Our documentation looks great, but a central element is still missing the :doc:`API Reference <api/index>`.

-----

.. admonition:: If you don't manage to run the tutorial
    :class: important

    .. code-block:: bash

        git reset --hard 85031f317632af1eea7381c1f2dfdd461fd7c53c