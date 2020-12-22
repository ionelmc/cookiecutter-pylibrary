{%- if cookiecutter.c_extension_support == 'cffi' %}
char* {{ cookiecutter.c_extension_function }}(int argc, char *argv[]) {
    if (argc) {
        int len, i,
            max = 0,
            pos = 0;
        for (i = 0; i < argc; i++) {
            len = strlen(argv[i]);
            if (len > max) {
                max = len;
                pos = i;
            }
        }
        return argv[pos];
    } else {
        return NULL;
    }
}
{% else %}
#include "Python.h"

static PyObject* {{ cookiecutter.c_extension_function }}(PyObject *self, PyObject *value) {
    PyObject *module;
    PyObject *module_dict;
    PyObject *len;
    PyObject *max;
    PyObject *args;
    PyObject *kwargs;
    PyObject *result;

{%- if cookiecutter.legacy_python == "yes" %}
    #if PY_MAJOR_VERSION < 3
      module = PyImport_ImportModule("__builtin__");
    #else
{%- endif %}
      module = PyImport_ImportModule("builtins");
{%- if cookiecutter.legacy_python == "yes" %}
    #endif
{%- endif %}
    if (!module)
        return NULL;

    module_dict = PyModule_GetDict(module);
    len = PyDict_GetItemString(module_dict, "len");
    if (!len) {
        Py_DECREF(module);
        return NULL;
    }
    max = PyDict_GetItemString(module_dict, "max");
    if (!max) {
        Py_DECREF(module);
        return NULL;
    }
    Py_DECREF(module);

    args = PyTuple_New(1);
    if (!args) {
        return NULL;
    }
    Py_INCREF(value);
    PyTuple_SetItem(args, 0, value);

    kwargs = PyDict_New();
    if (!kwargs) {
        Py_DECREF(args);
        return NULL;
    }
    PyDict_SetItemString(kwargs, "key", len);

    result = PyObject_Call(max, args, kwargs);

    Py_DECREF(args);
    Py_DECREF(kwargs);

    return result;
}

PyDoc_STRVAR({{ cookiecutter.c_extension_function }}_doc, "Docstring for {{ cookiecutter.c_extension_function }} function.");

static struct PyMethodDef module_functions[] = {
    {"{{ cookiecutter.c_extension_function }}", {{ cookiecutter.c_extension_function }}, METH_O, {{ cookiecutter.c_extension_function }}_doc},
    {NULL, NULL}
};

{%- if cookiecutter.legacy_python == "yes" %}
#if PY_MAJOR_VERSION >= 3
{%- endif %}
static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "{{ cookiecutter.package_name }}.{{ cookiecutter.c_extension_module }}", /* m_name */
    NULL,             /* m_doc */
    -1,               /* m_size */
    module_functions, /* m_methods */
    NULL,             /* m_reload */
    NULL,             /* m_traverse */
    NULL,             /* m_clear */
    NULL,             /* m_free */
};
{%- if cookiecutter.legacy_python == "yes" %}
#endif
{%- endif %}

static PyObject* moduleinit(void) {
    PyObject *module;

{%- if cookiecutter.legacy_python == "yes" %}
#if PY_MAJOR_VERSION >= 3
{%- endif %}
    module = PyModule_Create(&moduledef);
{%- if cookiecutter.legacy_python == "yes" %}
#else
    module = Py_InitModule3("{{ cookiecutter.package_name }}.{{ cookiecutter.c_extension_module }}", module_functions, NULL);
#endif
{%- endif %}

    if (module == NULL)
        return NULL;

    return module;
}

{%- if cookiecutter.legacy_python == "yes" %}
#if PY_MAJOR_VERSION < 3
PyMODINIT_FUNC init{{ cookiecutter.c_extension_module }}(void) {
    moduleinit();
}
#else
{%- endif %}
PyMODINIT_FUNC PyInit_{{ cookiecutter.c_extension_module }}(void) {
    return moduleinit();
}
{%- if cookiecutter.legacy_python == "yes" %}
#endif
{%- endif %}
{% endif %}
