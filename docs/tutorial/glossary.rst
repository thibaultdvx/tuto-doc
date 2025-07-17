Build a glossary
================

Here, we will quickly show how to automatically build a glossary with Sphinx.
It doesn't require any Sphinx extension.

1. Add terms in your glossary via the command ``:term:``. For example, in the docstring of ``SinglePlot``,
   change ``**RAS+**`` to ``:term:`RAS+```.

2. Create a glossary page at ``docs/glossary.rst``. Put the glossary in there via the ``.. glossary::`` command, and define
   your terms:

.. dropdown:: ``docs/glossary.rst``

    .. code-block:: rst

        Glossary
        ========

        .. glossary::
            :sorted:
            
            RAS+
                `<https://nipy.org/nibabel/coordinate_systems.html#naming-reference-spaces>`_

3. Add the glossary in the table of content in ``docs/index.rst``:

.. code-block:: rst

    .. toctree::
        :maxdepth: 1
        :hidden:

        installation
        getting_started
        user_guide/index
        auto_examples/index
        api/index
        glossary

4. Build your documentation. You should see the glossary page, with the definition of ``RAS+`` inside.

-----

.. admonition:: If you don't manage to run the tutorial
    :class: important

    .. code-block:: bash

        git reset --hard 5c5e3c6a1433b9b592f0b7919d7252550d797f60