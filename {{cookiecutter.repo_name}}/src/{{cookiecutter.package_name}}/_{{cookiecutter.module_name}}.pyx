# cython: linetrace=True, language_level=3str

def {{ cookiecutter.function_name }}(args):
    return max(args, key=len)
