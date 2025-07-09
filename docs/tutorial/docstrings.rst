# Writing docstrings

The very first step to document a Python project is to write **docstrings**.

To do that, I recommend the very useful VSCode extension [autodocstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring). It will automatically generate the structure
of your docstring, and add type hints and default values to it.

To have consistent documentations, we will work with the same docstring template.
To define the template:

1. Open VSCode settings (`⌘,` on macOS);
2. search for "autodocstring";
3. in `Auto Docstring: Docstring Format`, choose `numpy`.