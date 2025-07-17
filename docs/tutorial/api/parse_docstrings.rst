Parsing docstrings with Sphinx
==============================

One key functionality of Sphinx is that it can build automatically
the API Reference from docstrings. Let's do it step by step!

``autodoc`` extension
---------------------

The main actor here is the `autodoc <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_
extension. It is already installed with Sphinx, and to activate it, add it to your extensions in your ``conf.py``:

.. code-block:: python

    extensions = [
        "sphinx_design",
        "sphinx_copybutton",
        "myst_parser",
        "sphinx.ext.autodoc",
    ]

    templates_path = ["_templates"]
    exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

    autodoc_inherit_docstrings = False

.. note::
    You may have noticed that we have also added ``autodoc_inherit_docstrings = False``. This really is not an essential
    setting. Here, we use it because we don't want ``neuroplot.plot.multiple.MultiplePlot`` to inherit from
    ``neuroplot.plot.single.SinglePlot``'s docstrings.

Then, change your ``docs/api/index.rst``:

.. dropdown:: ``docs/api/index.rst``

    .. code-block:: rst

        API Reference
        =============

        ``neuroplot.plot``: Plotting neuroimages
        ----------------------------------------

        ``neuroplot.plot.single``
        *************************

        .. currentmodule:: neuroplot.plot.single

        .. autoclass:: SinglePlot

Build your documentation to see the results... Go to the ``API Reference`` section...
Tada! Sphinx used the docstring to build the documentation of ``SinglePlot``!

What just happened?

1. We told Sphinx where to find the class we want to document with ``.. currentmodule::``.
2. We told Sphinx to generate a documentation from the docstrings of ``SinglePlot`` with ``.. autoclass::``.

.. note::
    If it was a function to document, we would use ``.. autofunction::``.

But you may have noticed that we miss the methods of ``SinglePlot``. To fix this issue, just add
the ``:members:`` command:

.. dropdown:: ``docs/api/index.rst``

    .. code-block:: rst

        API Reference
        =============

        ``neuroplot.plot``: Plotting neuroimages
        ----------------------------------------

        ``neuroplot.plot.single``
        *************************

        .. currentmodule:: neuroplot.plot.single

        .. autoclass:: SinglePlot
            :members:

If you remember well, we also put docstrings in some ``__init__.py`` files. To include them in the documentation, use ``.. automodule::``:

.. dropdown:: ``docs/api/index.rst``

    .. code-block:: rst

        API Reference
        =============

        ``neuroplot.plot``: Plotting neuroimages
        ----------------------------------------

        .. automodule:: neuroplot.plot

        ``neuroplot.plot.single``
        *************************

        .. automodule:: neuroplot.single.plot

        .. currentmodule:: neuroplot.plot.single

        .. autoclass:: SinglePlot
            :members:

.. note::
    If may seem superfluous to include docstrings for modules. But even if you think that, it is still
    important to use ``.. automodule::`` because it will enable you to refer to this module anywhere via ``:py:mod:``.

Ok, now let's build the API Reference for the whole ``neuroplot`` package:

.. dropdown:: ``docs/api/index.rst``

    .. code-block:: rst

        API Reference
        =============

        ``neuroplot.plot``: Plotting neuroimages
        ----------------------------------------

        .. automodule:: neuroplot.plot

        ``neuroplot.plot.single``
        *************************

        .. automodule:: neuroplot.plot.single

        .. currentmodule:: neuroplot.plot.single

        .. autoclass:: SinglePlot
            :members:

        .. autoclass:: GIF
            :members:

        ``neuroplot.plot.multiple``
        ***************************

        .. automodule:: neuroplot.plot.multiple

        .. currentmodule:: neuroplot.plot.multiple

        .. autoclass:: MultiplePlot
            :members:

        ``neuroplot.transforms``: Transforming images before plotting
        -------------------------------------------------------------

        .. automodule:: neuroplot.transforms

        .. currentmodule:: neuroplot.transforms

        .. autoclass:: Noise
            :members:

        .. autoclass:: RescaleIntensity
            :members:

.. note::
    The other classes don't have docstrings yet, that's why their documentation is empty!

We reached our goal, but currently the API Reference is not very legible. Let's use Sphinx
tools to improve it.

``napoleon`` extension
----------------------

We are using NumPy style docstrings, and there is an extension developed to render well these kinds
of docstrings: `napoleon <https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html>`_.

To use it, simply add it in your ``conf.py``:

.. code-block:: python

    extensions = [
        "sphinx_design",
        "sphinx_copybutton",
        "myst_parser",
        "sphinx.ext.autodoc",
        "sphinx.ext.napoleon",
    ]

    templates_path = ["_templates"]
    exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

    autodoc_inherit_docstrings = False

    napoleon_custom_sections = [("Returns", "params_style")]

.. note::
    ``napoleon_custom_sections`` is not an essential setting. It is just to render well the ``Returns`` section.

``intersphinx`` extension
-------------------------

Have you noticed that when you click on ``plot()`` in "2D slices will be plotted via the method ``plot()``." in the documentation
of ``SinglePlot``, it will redirect you to the documentation of the ``plot`` method. The same goes for the mention of
``neuroplot.plot.multiple.MultiplePlot`` in the ``See Also`` section, as well as ``neuroplot.transforms`` in the description of
``transforms`` parameter. This is a great functionality offered by ``autodoc`` that
will enable you to cross-reference across your documentation.

But what about external references? For example, I would like ``matplotlib.pyplot.figure()`` (in the description of ``figsize``
parameter) to be linked to `matplotlib documentation <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure>`_.

A great solution is `intersphinx <https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html>`_. To use it, put
it in your ``conf.py``:

.. code-block:: python

    extensions = [
        "sphinx_design",
        "sphinx_copybutton",
        "myst_parser",
        "sphinx.ext.autodoc",
        "sphinx.ext.napoleon",
        "sphinx.ext.intersphinx",
    ]

    templates_path = ["_templates"]
    exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

    autodoc_inherit_docstrings = False

    napoleon_custom_sections = [("Returns", "params_style")]

    intersphinx_mapping = {
        "matplotlib": ("https://matplotlib.org/stable/", None),
    }

Build your documentation and watch the magic happen!

.. important::
    This functionality only works with **external libraries whose documentations
    are built with Sphinx**. Hopefully, this is the case for most of the common
    Python libraries!

``viewcode`` extension
----------------------

Lastly, a feature that I find very useful in a documentation is to have the source code easily accessible.
Once again, Sphinx comes with a built-in solution: `viewcode <https://www.sphinx-doc.org/en/master/usage/extensions/viewcode.html>`_.

You know the recipe. In your ``conf.py``:

.. code-block:: python

    extensions = [
        "sphinx_design",
        "sphinx_copybutton",
        "myst_parser",
        "sphinx.ext.autodoc",
        "sphinx.ext.napoleon",
        "sphinx.ext.intersphinx",
        "sphinx.ext.viewcode",
    ]

Build your documentation and try the functionality!

Well, I don't know about you, but I'm quite happy with the improvements we've just made. Nevertheless, I still find our
API Reference a bit messy. Imagine we have tens of classes to document... It is probably not a good idea to
put them all on the same page. So do we have to manually create one page for each of them? You probably have guessed
the answer... No! Sphinx offers another smart functionality: :doc:`autosummary <auto_summary>`.

-----

.. admonition:: If you don't manage to run the tutorial
    :class: important

    .. code-block:: bash

        git reset --hard 692644e93d81de77e8451f5019a883b253321656
