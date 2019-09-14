
Changelog
=========
{% set datestring = '<TODAY>' if cookiecutter.release_date == 'today' else cookiecutter.release_date %}
{{ cookiecutter.version }} ({{ datestring }})
{% for _ in cookiecutter.version %}-{% endfor %}-{% for _ in datestring %}-{% endfor %}

* First release on PyPI.
