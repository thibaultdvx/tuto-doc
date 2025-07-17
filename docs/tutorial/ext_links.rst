Manage external links
=====================

In a Sphinx documentation, you may have many references to external websites. To help you to
refer to these websites easily, the Sphinx extension `extlinks <https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html>`_
can be useful.

For example, imagine that you often refer to different sections of a website. Let's say ``nibabel``
documentation: https://nipy.org/nibabel/. One time you'll refer to this page: https://nipy.org/nibabel/gettingstarted.html;
another time to this one: https://nipy.org/nibabel/coordinate_systems.html.

It is redundant to always put the base pattern. Besides, if the domain name changes, we would have to change
manually all the urls.

``extlinks`` helps with that: you can define common external links in the ``docs/conf.py`` via ``extlinks`` (don't forget to also activate the extension
by putting ``sphinx.ext.extlinks`` in the extensions list):

.. code-block:: rst

    extensions = [
        "sphinx_design",
        "sphinx_copybutton",
        "myst_parser",
        "sphinx.ext.autodoc",
        "sphinx.ext.napoleon",
        "sphinx.ext.intersphinx",
        "sphinx.ext.viewcode",
        "sphinx.ext.autosummary",
        "sphinx.ext.extlinks",
        "sphinx_gallery.gen_gallery",
        "sphinxcontrib.bibtex",
    ]

    templates_path = ["_templates"]
    exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

    autodoc_inherit_docstrings = False

    napoleon_custom_sections = [("Returns", "params_style")]

    intersphinx_mapping = {
        "matplotlib": ("https://matplotlib.org/stable/", None),
    }

    from pathlib import Path

    sphinx_gallery_conf = {
        "examples_dirs": "../examples",
        "gallery_dirs": "auto_examples",
        "backreferences_dir": Path("api", "generated"),  # where mini-galleries are stored
        "doc_module": (
            "neuroplot",
        ),  # generate mini-galleries for all the objects in neuroplot
    }

    bibtex_bibfiles = ["references.bib"]

    extlinks = {
        "nibabel": (
            "https://nipy.org/nibabel/%s",
            None,
        ),
    }

The ``%s`` in ``https://nipy.org/nibabel/%s`` means that ``https://nipy.org/nibabel/`` is our base pattern.

Now we can use this base pattern via the new command ``:nibabel:``. For example, change your ``docs/glossary.rst`` to:

.. code-block:: rst

    Glossary
    ========

    .. glossary::
        :sorted:
        
        RAS+
            :nibabel:`coordinate_systems.html#naming-reference-spaces`

And rebuild the documentation... Nothing changed! We are still redirected to https://nipy.org/nibabel/coordinate_systems.html#naming-reference-spaces

In the same way as with raw links, you can also "rename" the link:

.. code-block:: rst

    Glossary
    ========

    .. glossary::
        :sorted:
        
        RAS+
            See :nibabel:`nibabel <coordinate_systems.html#naming-reference-spaces>`.

-----

.. admonition:: If you don't manage to run the tutorial
    :class: important

    .. code-block:: bash

        git reset --hard 7dfb89847865b227e56a0461582acb5dfb5aba21