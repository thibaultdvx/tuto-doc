Read the Docs
=============

Let's get straight to the point. To deploy your documentation with `Read the Docs <https://about.readthedocs.com/>`_:

1. Create a ``.readthedocs.yaml`` at the root of your project, on the ``main`` branch (no need to
   do it here, there is already one). This file will tell Read the Docs what to do to build the
   documentation.

.. dropdown:: ``.readthedocs.yaml``

    .. code-block:: yaml

        # Read the Docs configuration file
        # See https://docs.readthedocs.io/en/stable/config-file/v2.html for details

        # Required
        version: 2

        # Set the OS, Python version, and other tools you might need
        build:
            os: ubuntu-24.04
            tools:
                python: "3.12"
            jobs:
                post_create_environment:
                    - pip install poetry
                    - poetry config virtualenvs.create false
                    - . "$READTHEDOCS_VIRTUALENV_PATH/bin/activate" && poetry install --with docs

        # Build documentation in the "docs/" directory with Sphinx
        sphinx:
            configuration: docs/conf.py

2. Got to https://about.readthedocs.com/.
3. Log in with your GitHub account: **Log In > Read the Docs Community > Log in using GitHub**.
4. Click on **Add project**, and fill the fields with:
    - *Repository name*: select ``<github-username>/tuto-doc``
    - *Name*: ``NeuroPlot-<github-username>``
    - *Default branch*: ``main``

And, here we go! Let's just wait a few minutes that Read the Docs deploy the website, which will be accessible at:
``https://neuroplot-{github-username}.readthedocs.io/``.

Once on your website, on the bottom right, click on the green button **latest**. These are the
available versions of our documentation. Currently, the only version available is *latest*, which is the latest
version on our default branch. We would like to have several versions available:

- *latest*, with our latest changes on ``main``;
- *stable*, corresponding to the last stable version;
- an historic of the versions.

In Git, the notion of "version" of a project is represented via `tags <https://docs.github.com/en/repositories/releasing-projects-on-github/viewing-your-repositorys-releases-and-tags>`_.
You can go to any branch of your project, to any commit, and create a tag saying "this is version xxx".
For example:

1. Checkout to ``main``
2. Run the command ``git tag v0.2.0``
3. Then, checkout to ``doc``
4. Run ``git tag v0.1.0``
5. Then, ``git push origin --tag``

You have just created 2 tags, one from ``main`` and one from ``doc``.

If you come back to the Read the Docs dashboard, you will see that a new version of your project appeared: *stable*,
which corresponds to the documentation build from your **latest version** (``v0.2.0`` here).

If you go to your documentation, you can see that you have now two versions available: *stable* and *latest*.

To add the historic of the versions:

1. in the Read the Docs dashboard, click on **Add version**;
2. select the version you want to have in the history;
3. check the box **Active**;
4. click on **Update version**.

Finally, give Read the Docs time to build the old versions, and go to your online documentation to see the result! 