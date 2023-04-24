from json import dumps

from jinja2.ext import Extension


def jsonquote(value):
    return dumps(value, ensure_ascii=False)


class JsonQuoteExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)
        environment.filters['jsonquote'] = jsonquote
