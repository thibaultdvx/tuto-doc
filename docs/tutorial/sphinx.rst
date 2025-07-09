Getting started with Sphinx
===========================

As mentioned earlier, Sphinx is a really convenient tool to build the **documentation for
a Python API**, because of the **many functionalities** it offers, but also because it is **easy to
handle**.

To install Sphinx, use ``poetry``:

.. code-block::

    poetry add sphinx --group docs

.. note::

    Here, we have just created a group of dependencies named "docs", which will contain
    the documentation-specific dependencies. Have a look at your ``pyproject.toml``.

Then, create a ``docs`` folder:

.. code-block::

    mkdir docs
    cd docs

And finally, run:

.. code-block::

    sphinx-quickstart

It will ask you several questions. You can give the following answer:

.. code-block::

    > Separate source and build directories (y/n) [n]: y
    > Project name: NeuroPlot
    > Author name(s): ARAMIS Lab
    > Project release []: 0.1.0
    > Project language [en]: en

This ``latter`` command will initialize your documentation. You should get something like that:

.. code-block::

    docs
    ├── _static
    ├── _templates
    ├── conf.py
    ├── index.rst
    ├── make.bat
    └── Makefile

We will understand these files as we progress in the tutorial. You can start with opening ``index.rst``.
You will find in there the content of the home page of your documentation.

To prove it to you, we will build our documentation:

.. code-block::

    make html

You should now have some contents in the ``_build`` folder. There are *html* files inside. To read them
we will open the documentation locally with our web browser:

.. code-block::

    python -m http.server 8888 --directory '_build/html'

An then open http://localhost:8888/ in your web browser. You should be able to see your documentation
for the first time! We will now :doc:`customize it <configure>`.

.. warning::

    You don't want to track the generated *html* files with Git. That's why it is important to
    add a ``.gitignore`` file in your ``docs`` folder and put ``/_build`` inside.

.. tip::

    We will build the documentation many times locally. So, in order not to have to run every time the
    ``python -m http.server`` command, you can open another terminal, run:

    .. code-block::
        
        cd docs
        python -m http.server 8888 --directory '_build/html'

    and let it run in the background.

    By doing so, when you make a change to your documentation, you just have to run ``make html``,
    and then refresh the http://localhost:8888/ page in your web browser.

.. admonition:: Under the hood
    :class: hint

    The command ``make html`` is defined in the ``Makefile``. It is a convenient alias for the command
    ``sphinx-build -M html . _build``.