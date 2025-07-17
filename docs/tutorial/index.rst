Documentation tutorial
======================

Dev meeting, July 2025.

.. toctree::
   :maxdepth: 2
   :numbered:
   
   sphinx
   write
   configure
   api/index
   deploy/index

.. toctree::
   :caption: Bonus
   :maxdepth: 1
   
   examples
   glossary
   references
   ext_links

Introduction
------------

The goal of this tutorial is to learn how to publish a documentation for your Python
projects. And we will prove you it's not a big deal! Have a quick look at
`what you will have built in an hour <https://www.aramislab.fr/tuto-doc/>`_.

Needless to say that if you are developing a software, a public documentation
is mandatory. And if you are a PhD, it is also an interesting knowledge to have.
It will give credit to your projects, and greatly facilitate collaboration and
handover to new PhDs.

Let's get started!

.. _documentation-overview:

Overview of a documentation
***************************

Let's define the scope of this tutorial: we have a **Python API** that we want
to document.

To begin, let's take inspiration from the community. Among other well known
Python libraries, you've probably already to `scikit-learn documentation <https://scikit-learn.org/stable/>`_,
or `numpy's <ttps://numpy.org/doc/stable>`_. Another that often inspires me in
`niilearn's <https://nilearn.github.io/stable>`_.

Even if these documentations differ on some points, we can see common patterns. More precisely,
there are some sections that you will often find in an API documentation:

- An ``installation`` section: the first and most fundamental section with instructions to
  install the package properly.
- A ``getting started`` section: a quick overview of the main features of your package. This is where your "sell" your project!
- ``examples``: concrete examples that the user should be able to run on his own.
- A ``user guide``: a section where you present in details all the features of the package.
  All the well know Python projects have an exhaustive user guide, but this section is
  really time-consuming to work, so I think it shouldn't be your priority.
- An ``API Reference``: a section where you document the public Python objects of your API
  (e.g. your functions and the parameters that they take). We will see that this section is
  really easy to build from your docstrings.
- A ``contribution guide``: if you want to encourage people to contribute to your project.

.. note::

    I you ask me what is the priority, I would say that an ``installation`` section, a ``getting started`` section,
    and an ``API Reference`` are a good start. Secondly, I would feed the ``examples``. The ``contribution guide``
    and particularly the ``user guide`` are a bit more time-consuming to write and are expected for more
    advanced project.

Technical baggage to publish a documentation
********************************************

To publish a documentation, there are three steps:

1. **write** the documentation;
2. **build** it: convert your documentation to a publishable website (i.e. a set of *html*, *css*, *js*, etc. files);
3. **deploy** it: publish the website on the internet.

Now that I've mentioned *html*, *css*, and *js*, I can see that you are afraid. Fortunately, modern tools
take care of the nasty things and **build automatically** your website from the documentation that
you have written in user-friendly format like `Markdown <https://www.markdownguide.org/>`_.

Two popular tools are `Sphinx <https://www.sphinx-doc.org/en>`_ and `MkDocs <https://www.mkdocs.org/>`_.
MkDocs is more than enough to build a documentation only from markdown files, but **in the case of
an API, we will prefer Sphinx**, that offers really convenient functionalities, such as building automatically
the API Reference from docstrings.

.. note::

    If your software is not an API, e.g. a command-line interface, MkDocs may be the right choice.
    Have a look at `Clinica documentation <https://aramislab.paris.inria.fr/clinica/docs/public/latest/>`_
    to have an example of what you can do with MkDocs.


To **deploy** our website, we will try two options: `GitHub Pages <https://docs.github.com/en/pages/quickstart>`_ and
`Read the Docs <https://about.readthedocs.com/>`_.

Today's tutorial
----------------

Now that you have all the required knowledge to start the tutorial, let's introduce our use case.

We will work on a toy Python library, called ``neuroplot``, focused on neuroimaging data visualization.
This library is functional, and you can see some usage examples in the :doc:`example section <../auto_examples/index>`,
but we will start from a checkpoint when there was no documentation at all (not even docstrings!).
Our goal is thus to publish a documentation from scratch!

Clone the repo
**************

The repository of ``neuroplot`` is available `here <https://github.com/aramis-lab/tuto-doc>`_.

The first step of the tutorial is to **fork the repository** (make sure you fork all the branches
by unchecking the box "Copy the main branch only"), and then to **clone it**.
Then checkout to the ``code`` branch, and create a new branch from the latter:

.. code-block:: bash

    git checkout code
    git checkout -b tutorial

This is the starting point of the tutorial. All the files that you will find are related
to Python, and there is nothing related to documentation.

The Python architecture of the project is very simple and looks like this:

.. code-block:: text

    src/neuroplot
    ├── __init__.py
    ├── plot
    │   ├── __init__.py
    │   ├── multiple
    │   │   ├── __init__.py
    │   │   └── multiple_plot.py
    │   └── single
    │       ├── __init__.py
    │       ├── gif.py
    │       └── single_plot.py
    └── transforms
        ├── __init__.py
        ├── noise.py
        ├── rescale_intensity.py
        └── to_orientation.py

Create your environment
***********************

You know the recipe: when you start working with a new project, it is highly encouraged
to create a new Python environment. To do that, put yourself in the ``tuto-doc`` folder, and run:

.. code-block:: bash

    conda env create -f environment.yml
    conda activate tuto-doc

Then, install the required dependencies with ``poetry``:

.. code-block:: bash

    poetry install

.. dropdown:: Install ``poetry`` on macOS

    .. code-block:: bash

        brew install pipx
        pipx ensurepath
        pipx install poetry

Check that everything is working by running:

.. code-block:: bash

    poetry run pytest tests/unittests

So far, so good? Great! Let's get into the nitty-gritty, starting with :doc:`installing Sphinx <sphinx>`.

.. important::

    At the end of each step of the tutorial, we will give you the hash of a git commit that will
    lead you to the point you should have reached at the end of this step.

    For example, if you don't manage to finish :doc:`step 1 <sphinx>`, this will lead you to the
    expected result:

    .. code-block:: bash

        git checkout --hard da8cd18eb135f909244f70a7d4f6f9e0dff45a3c
