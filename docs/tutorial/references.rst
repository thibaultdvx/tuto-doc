Manage references with Sphinx
=============================

Here, we will see how to manage references using `sphinxcontrib-bibtex <https://sphinxcontrib-bibtex.readthedocs.io/>`_.

1. Install ``sphinxcontrib-bibtex``:

.. code-block:: bash

    poetry add sphinxcontrib-bibtex --group docs

2. Update your ``docs/conf.py`` to activate the extension, and tell Sphinx where are your references
   via ``bibtex_bibfiles``:

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

3. Put your references in ``docs/references.bib``:

.. dropdown:: ``docs/references.bib``

    .. code-block:: bib

        @Article{Harris:2020,
            title         = {Array programming with {NumPy}},
            author        = {Charles R. Harris and K. Jarrod Millman and St{\'{e}}fan J.
                            van der Walt and Ralf Gommers and Pauli Virtanen and David
                            Cournapeau and Eric Wieser and Julian Taylor and Sebastian
                            Berg and Nathaniel J. Smith and Robert Kern and Matti Picus
                            and Stephan Hoyer and Marten H. van Kerkwijk and Matthew
                            Brett and Allan Haldane and Jaime Fern{\'{a}}ndez del
                            R{\'{i}}o and Mark Wiebe and Pearu Peterson and Pierre
                            G{\'{e}}rard-Marchant and Kevin Sheppard and Tyler Reddy and
                            Warren Weckesser and Hameer Abbasi and Christoph Gohlke and
                            Travis E. Oliphant},
            year          = {2020},
            month         = sep,
            journal       = {Nature},
            volume        = {585},
            number        = {7825},
            pages         = {357--362},
            doi           = {10.1038/s41586-020-2649-2},
            publisher     = {Springer Science and Business Media {LLC}},
            url           = {https://doi.org/10.1038/s41586-020-2649-2}
        }

        @Article{Hunter:2007,
            Author    = {Hunter, J. D.},
            Title     = {Matplotlib: A 2D graphics environment},
            Journal   = {Computing in Science \& Engineering},
            Volume    = {9},
            Number    = {3},
            Pages     = {90--95},
            abstract  = {Matplotlib is a 2D graphics package used for Python for
            application development, interactive scripting, and publication-quality
            image generation across user interfaces and operating systems.},
            publisher = {IEEE COMPUTER SOC},
            doi       = {10.1109/MCSE.2007.55},
            year      = 2007
        }

4. In your documentation, you can know refer to the references in the ``docs/references.bib``. For example,
   change the docstring of ``neuroplot.plot.single.single_plot.SinglePlot`` to:

.. dropdown:: ``neuroplot.plot.single.single_plot.SinglePlot`` docstring

    .. code-block:: python

        """
        To plot a single neuroimage.

        2D slices will be plotted via the method :py:meth:`plot`. The user can choose which anatomical axes to plot,
        and which slice to plot along the axes.

        The title of the figure can be changed between plots using :py:meth:`set_title`.

        Just a random reference to :footcite:t:`Harris:2020`. And another to Matplotlib\\ :footcite:`Hunter:2007`.

        Parameters
        ----------
        axes : int | Sequence[int] | None, default=None
            The axis (or axes) to plot, among ``0`` (sagittal axis), ``1`` (coronal) or ``2`` (axial).
            Can be passed as a single axis, or a list of axes. If ``None``, the three axes will be plotted.
        slices : int | Sequence[int] | None, default=None
            The slice to plot for each axis. If ``None``, the middle slice will be plotted. Otherwise, the **number
            of slices passed must be equal to the number of plotted axes** (equal to :math:`3` if ``axes=None``).
        transforms : Sequence[Callable[[np.ndarray], np.ndarray]] | None, default=None
            Potential transforms to apply to the image before plotting. See :py:mod:`neuroplot.transforms`.

            .. important::
                No matter the transforms passed, the image will first be reoriented to the :term:`RAS+` coordinate system.

        figsize : tuple[float, float] | None, default=None
            The size of the figure. See :py:func:`matplotlib.pyplot.figure` for more details.
        title : str | None, default=None
            A potential title for the figures that will be plotted.

        Raises
        ------
        AssertionError
            If the number of slices passed is not equal to the number of plotted axes.

        Examples
        --------
        .. code-block:: python

            from neuroplot.plot.single import SinglePlot
            from neuroplot.transforms import RescaleIntensity

            plotter = SinglePlot(axes=[0, 2], slices=[55, 167], transforms=[RescaleIntensity()])

        .. code-block:: python

            >>> plotter.set_title("A first image")
            >>> plotter.plot("data/example_1.nii.gz")

        .. code-block:: python

            >>> plotter.set_title("Another image")
            >>> plotter.plot("data/example_2.nii.gz")

        See Also
        --------
        :py:class:`neuroplot.plot.multiple.MultiplePlot`
            To plot multiple neuroimages in a grid of subplots.

        References
        ----------
        .. footbibliography::
        """

Notice that we added some citations via the sentence 
``Just a random reference to :footcite:t:`Harris:2020`. And another to Matplotlib\\ :footcite:`Hunter:2007`.``, but we also
add a ``References`` section at the end of the docstring.

.. note::
    ``:footcite:t:`` and ``:footcite:`` are two different ways of citing, among others. See `sphinxcontrib-bibtex documentation <https://sphinxcontrib-bibtex.readthedocs.io/en/latest/usage.html#roles-and-directives>`_
    for more details.

5. Build your documentation. In the documentation of ``SinglePlot``, you should see your citations.

-----

.. admonition:: If you don't manage to run the tutorial
    :class: important

    .. code-block:: bash

        git reset --hard fdfd9a465e5bd52c1b35b36298fb15e42d0a8baa