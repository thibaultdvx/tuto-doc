GitHub Pages
============

`GitHub Pages <https://docs.github.com/en/pages/quickstart>`_ offers a really easy way to deploy
your documentation.

To use this functionality, go on the GitHub of your forked repository, then go to
**Settings > Pages > Build and deployment > Source**, and select **GitHub Actions**.

We won't go into the details, but a `GitHub Action <https://docs.github.com/en/actions>`_ is a
**task that is triggered every time a certain event occurs**. The task and the triggering event are defined
in a **workflow**, that you put in the ``.github/workflows`` folder of your repository.

Here our task is "building and deploying the documentation", and our event is "every time I push on
the ``main`` branch".

Well, here is the **workflow** associated to this action:

.. code-block:: yaml

    name: documentation

    on:
        push:
            branches: ["main"]

    permissions:
        contents: read
        pages: write
        id-token: write

    jobs:
        build:
            runs-on: ubuntu-latest
            steps:
                - uses: actions/checkout@v4
                - uses: snok/install-poetry@v1
                - uses: actions/setup-python@v5
                    with:
                        python-version: '3.12'
                - name: Install package
                    run: poetry install
                - name: Sphinx build
                    run: poetry run sphinx-build -M html docs docs/_build
                - name: Upload artifact
                    uses: actions/upload-pages-artifact@v3
                    with:
                        path: docs/_build/html

        deploy:
            environment:
                name: github-pages
                url: ${{ steps.deployment.outputs.page_url }}
            runs-on: ubuntu-latest
            needs: build
            steps:
                - name: Deploy to GitHub Pages
                    id: deployment
                    uses: actions/deploy-pages@v4

.. important::
    It is important to tell GitHub to only trigger the workflow when we push on
    our ``main`` branch. Otherwise, if we work on other branches, for example to develop
    a new feature, the public documentation will change every time we push something on
    these branches. So, with GitHub Pages, **make sure your public documentation relies on the most stable
    branch**.

In your forked repository, you already have this workflow in ``.github/workflows/build_and_deploy.yml`` of your ``main``
branch, so no need to add it.

To trigger the deployment, you may need to push something on your ``main`` branch (for example
merge the work you just did on the ``tutorial`` branch).

Then, your documentation should be available at ``https://<github-username>.github.io/tuto-doc``!

.. raw:: html

   <br><br>

As you just saw, GitHub Pages makes it very easy to publicly deploy your documentation. But there is one
main drawback: **there can be only one version of your documentation**. More precisely:

- you can't have different documentations for different branches;
- once you have updated your main branch, you can't see the old versions of the documentation.

It can be a real handicap if you plan to maintain your package regularly, because the users won't
use necessarily the latest version of your code.

That's why GitHub Pages is not used by common Python libraries, which have turned instead to
:doc:`Read the Docs <read_the_docs>`.
