from json import dumps

from jinja2.ext import Extension


def jsonify(obj, indent: int = 4) -> str:
    return dumps(obj, sort_keys=True, indent=indent, ensure_ascii=False)


class PrettyJsonifyExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)
        environment.filters['jsonify'] = jsonify
