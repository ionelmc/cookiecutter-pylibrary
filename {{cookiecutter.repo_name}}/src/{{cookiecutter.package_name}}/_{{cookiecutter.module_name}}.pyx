# cython: linetrace=True, freethreading_compatible=True

def {{ cookiecutter.function_name }}(args):
    return max(args, key=len)
