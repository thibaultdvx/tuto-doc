Going further with ``autosummary``
==================================

To recap:

- we have a first draft for our API Reference, but it is messy;
- to improve it, we would like all the classes/functions of the library to have their own
  documentation pages;
- but we don't want to create all the pages manually.

Hopefully, Sphinx extension `autosummary <https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html>`_
can take care of this:

1. Activate the extension in your ``conf.py``:

.. code-block:: python

    extensions = [
        "sphinx_design",
        "sphinx_copybutton",
        "myst_parser",
        "sphinx.ext.autodoc",
        "sphinx.ext.napoleon",
        "sphinx.ext.intersphinx",
        "sphinx.ext.viewcode",
        "sphinx.ext.autosummary",
    ]

2. Define the template for your pages generated automatically. Here, we tell Sphinx to generate
   all the documentation pages on Python classes according to a specific template. Create a file
   in ``docs/_templates/autosummary/class.rst``:

.. dropdown:: ``docs/_templates/autosummary/class.rst``

    .. code-block:: rst

        {{ fullname }}
        {{ underline }}

        .. currentmodule:: {{ module }}

        .. autoclass:: {{ objname }}
            :members:

.. note::
    We could also create a template for documentation of Python functions in ``docs/_templates/autosummary/function.rst``.

3. Use the command ``.. autosummary::`` in your ``docs/api/index.rst``:

.. dropdown:: ``docs/api/index.rst``

    .. code-block:: rst

        API Reference
        =============

        .. autosummary::
            :toctree: generated/
            :nosignatures:
            :template: autosummary/class.rst
            
            neuroplot.plot.single.SinglePlot
            neuroplot.plot.single.GIF
            neuroplot.plot.multiple.MultiplePlot
            neuroplot.transforms.Noise
            neuroplot.transforms.RescaleIntensity

4. Build your documentation!

.. warning::
    ``autosummary`` will generate files in ``docs/api/generated``. You don't want to track these files. So create a ``docs/api/.gitignore``
    file and put ``/generated`` inside.

.. note::
    ``:nosignatures:`` is not essential here. You can try without and see what you prefer!

Improvements
------------

With classes from both ``neuroplot.plot`` and ``neuroplot.transforms`` on the same page, I feel like we are mixing up apples and pears.
Let's rather build an ``autosummary`` for each module independently:

1. Create a ``docs/api/plot.rst`` file, dedicated to ``neuroplot.plot``:

.. dropdown:: ``docs/api/plot.rst``

    .. code-block:: rst

        ``neuroplot.plot``: Plotting neuroimages
        ========================================

        .. automodule:: neuroplot.plot

        ``neuroplot.plot.single``
        -------------------------

        .. automodule:: neuroplot.plot.single

        .. currentmodule:: neuroplot.plot.single

        .. autosummary::
            :toctree: generated/
            :nosignatures:
            :template: autosummary/class.rst

            SinglePlot
            GIF

        ``neuroplot.plot.multiple``
        ---------------------------

        .. automodule:: neuroplot.plot.multiple

        .. currentmodule:: neuroplot.plot.multiple

        .. autosummary::
            :toctree: generated/
            :nosignatures:
            :template: autosummary/class.rst

            MultiplePlot

2. Create a ``docs/api/transforms.rst`` file, dedicated to ``neuroplot.transforms``:

.. dropdown:: ``docs/api/transforms.rst``

    .. code-block:: rst

        ``neuroplot.transforms``: Transforming images before plotting
        =============================================================

        .. automodule:: neuroplot.transforms

        .. currentmodule:: neuroplot.transforms

        .. autosummary::
            :toctree: generated/
            :nosignatures:
            :template: autosummary/class.rst

            Noise
            RescaleIntensity

3. Change ``docs/api/index.rst`` to redirect to ``docs/api/plot.rst`` or
   ``docs/api/transforms.rst``:

.. dropdown:: ``docs/api/transforms.rst``

    .. code-block:: rst

        API Reference
        =============

        .. toctree::
            :maxdepth: 1
            
            plot
            transforms

4. Build the documentation!

That's it! We have finished our API Reference, and therefore our documentation! It certainly doesn't look complete,
but this is only because we still have many docstrings to write. But I hope you got the idea!

Finally, now that our documentation is finished, we must :doc:`deploy it <../deploy/index>` so that
it is publicly available.

-----

.. admonition:: If you don't manage to run the tutorial
    :class: important

    .. code-block:: bash

        git reset --hard 9a105d76b8119b0f96bbaef15b52a6ebb711d03e