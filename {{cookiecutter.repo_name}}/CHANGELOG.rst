
Changelog
=========
{% set datestring = 'hooks/post_gen_project.py replace this with datetime.date.today().strftime("%Y-%m-%d")' if cookiecutter.release_date == 'today' else cookiecutter.release_date %}
{{ cookiecutter.version }} ({{ datestring }})
{% for _ in cookiecutter.version %}-{% endfor %}--{{ '-' * (4+1+2+1+2 if cookiecutter.release_date == 'today' else datestring|length) }}-

* First release on PyPI.
