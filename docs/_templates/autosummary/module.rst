{{ fullname }}
{{ underline }}

.. automodule:: {{ fullname }}

.. currentmodule:: {{ fullname }}

{% if modules %}
.. autosummary::
    :toctree:

{% for item in modules %}
    {{ item }}
{% endfor %}
{% endif %}

{% if classes %}
.. autosummary::
    :toctree:

{% for item in classes %}
    {{ item }}
{% endfor %}
{% endif %}

{% if functions %}
.. autosummary::
    :toctree:

{% for item in functions %}
    {{ item }}
{% endfor %}
{% endif %}