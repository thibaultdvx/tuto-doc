Generate an example gallery
===========================

Here, we want to create an example gallery like :doc:`this one <../auto_examples/index>`.
To do this, we will use `sphinx-gallery <https://sphinx-gallery.github.io/>`_.

Configure ``sphinx-gallery``
----------------------------

1. Install the extension:

.. code-block:: bash

    poetry add sphinx-gallery --group docs

2. Update your ``docs/conf.py``. We will activate the ``sphinx-gallery`` extension, and tell Sphinx
   where are our examples, and where we want the example gallery pages to be generated, via the
   variable ``sphinx_gallery_conf``:

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
        "sphinx_gallery.gen_gallery",
    ]

    templates_path = ["_templates"]
    exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

    autodoc_inherit_docstrings = False

    napoleon_custom_sections = [("Returns", "params_style")]

    intersphinx_mapping = {
        "matplotlib": ("https://matplotlib.org/stable/", None),
    }

    sphinx_gallery_conf = {
        "examples_dirs": "../examples",
        "gallery_dirs": "auto_examples",
    }

3. At the source of your project create an ``examples`` folder.
   To be valid, this folder must contain at least a file named ``GALLERY_HEADER.rst``. We will simply put
   a title for our gallery in it:

.. dropdown:: ``examples/GALLERY_HEADER.rst``

    .. code-block:: rst

        Examples
        ========

4. Add your gallery main page in the table of content in ``docs/index.rst``. The main page of your generated gallery will be named
   ``docs/auto_examples/index.rst``.

.. code-block:: rst

    .. toctree::
        :maxdepth: 1
        :hidden:

        installation
        getting_started
        user_guide/index
        auto_examples/index
        api/index

5. Build your documentation. You should now see your example gallery, which is currently empty!

.. warning::
    We don't want to track the gallery generated. So, put ``/auto_examples``
    in your ``docs/.gitignore``. Besides, ``sphinx-gallery`` also generates a file named ``sg_execution_times.rst``; put also
    this file in your ``docs/.gitignore``.

Write examples
--------------

All your examples should be created in the ``examples`` folder. Otherwise, ``sphinx-gallery`` won't see them.

Let's create an example in ``examples/plot_single_image.py``:

.. dropdown:: ``examples/plot_single_image.py``

    .. code-block:: python

        """
        Plot a 3D image
        ===============

        This example shows how to plot a single 3D image.
        """

        # %%
        # Download the images
        # -------------------

        import tarfile
        import urllib.request
        from pathlib import Path

        url = "https://aramislab.paris.inria.fr/clinicadl/files/handbook_2023/data_oasis/BIDS_example.tar.gz"
        data_path = Path("data")
        data_path.mkdir(exist_ok=True)
        download_path = data_path / "BIDS_example.tar.gz"

        urllib.request.urlretrieve(url, download_path)
        with tarfile.open(download_path, "r:gz") as tar:
            tar.extractall(path=data_path)

        image_path = (
            data_path
            / "data_oasis"
            / "BIDS_example"
            / "sub-OASIS10016"
            / "ses-M000"
            / "anat"
            / "sub-OASIS10016_ses-M000_T1w.nii.gz"
        )
        image_path.exists()

        # %%
        # Plot the raw image
        # ------------------
        #
        # Let's plot the sagittal and coronal axes of the image:

        from neuroplot.plot.single import SinglePlot

        plotter = SinglePlot(axes=[0, 1])
        plotter.plot(img_path=image_path)

        # %%
        # Add transforms
        # ---------------
        #
        # Let's add some noise to the image:

        from neuroplot.transforms import Noise

        plotter = SinglePlot(axes=[0, 1], transforms=[Noise(std=200)])
        plotter.plot(img_path=image_path)

An example should always start with a docstring, that defines the header, and then contains
Python code. We can also add some ``rst`` syntax between Python blocks. More details `here <https://sphinx-gallery.github.io/stable/syntax.html>`_.

Rebuild your documentation and see how ``sphinx-gallery`` ran the example and saved the outputs to display them
in the generated example page.

.. important::
    By default, ``sphinx-gallery`` will only show the examples whose name starts with ``plot_``.

.. warning::
    Our example downloads data in ``examples/data``, and you ou don't want to track these data. So, create a ``examples/.gitignore``
    and put ``/data`` inside.

Generates mini-galleries
------------------------

Now, we would like to generate a mini-gallery for each Python object in our API Reference. This mini-gallery will contain all
the examples that use this Python object. To do that, we will follow `sphinx-gallery instructions <https://sphinx-gallery.github.io/stable/configuration.html#add-mini-galleries-for-api-documentation>`_:

1. Update your ``docs/conf.py``:

.. code-block:: python

    from pathlib import Path

    sphinx_gallery_conf = {
        "examples_dirs": "../examples",
        "gallery_dirs": "auto_examples",
        "backreferences_dir": Path("api", "generated"),  # where mini-galleries are stored
        "doc_module": (
            "neuroplot",
        ),  # generate mini-galleries for all the objects in neuroplot
    }

2. Modify your ``docs/_templates/autosummary/class.rst`` template, so that ``autosummary`` adds the mini-galleries
   at the end of your documentation pages:

.. code-block:: rst

    {{ fullname }}
    {{ underline }}

    .. currentmodule:: {{ module }}

    .. autoclass:: {{ objname }}
        :members:

    .. include:: {{fullname}}.examples

3. Build the documentation and have a look at the documentation page of ``SinglePlot``. You should see the
   mini-gallery at the bottom of the page!

-----

.. admonition:: If you don't manage to run the tutorial
    :class: important

    .. code-block:: bash

        git reset --hard f5b362a44e4c3ddf92f4bf6c89d1df0b9dcf5f0a