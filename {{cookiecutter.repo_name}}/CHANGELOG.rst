
Changelog
=========
{% set datestring -%}
{% if cookiecutter.release_date == 'today' -%}
{% now 'utc', '%Y-%m-%d' %}
{%- else %}{{ cookiecutter.release_date }}{% endif %}
{%- endset %}
{{ cookiecutter.version }} ({{ datestring }})
{% for _ in cookiecutter.version %}-{% endfor %}--{{ '-' * (datestring|length) }}-

* First release on PyPI.
