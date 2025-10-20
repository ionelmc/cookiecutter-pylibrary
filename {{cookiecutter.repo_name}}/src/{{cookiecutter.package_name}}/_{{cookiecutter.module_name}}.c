{%- if cookiecutter.c_extension_support == 'cffi' %}
char* {{ cookiecutter.function_name }}(int argc, char *argv[]) {
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
{%- else -%}
#include "Python.h"

static PyObject* {{ cookiecutter.function_name }}(PyObject *self, PyObject *value) {
    PyObject *module;
    PyObject *module_dict;
    PyObject *len;
    PyObject *max;
    PyObject *args;
    PyObject *kwargs;
    PyObject *result;
    module = PyImport_ImportModule("builtins");
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

PyDoc_STRVAR({{ cookiecutter.function_name }}_doc, "Docstring for {{ cookiecutter.function_name }} function.");

static struct PyMethodDef module_functions[] = {
    {"{{ cookiecutter.function_name }}", {{ cookiecutter.function_name }}, METH_O, {{ cookiecutter.function_name }}_doc},
    {NULL, NULL}
};

static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "{{ cookiecutter.package_name }}._{{ cookiecutter.module_name }}", /* m_name */
    NULL,             /* m_doc */
    -1,               /* m_size */
    module_functions, /* m_methods */
    NULL,             /* m_reload */
    NULL,             /* m_traverse */
    NULL,             /* m_clear */
    NULL,             /* m_free */
};

static PyObject* moduleinit(void) {
    PyObject *module;

    module = PyModule_Create(&moduledef);

    if (module == NULL)
        return NULL;

#ifdef Py_GIL_DISABLED
    PyUnstable_Module_SetGIL(m, Py_MOD_GIL_NOT_USED);
#endif

    return module;
}

PyMODINIT_FUNC PyInit__{{ cookiecutter.module_name }}(void) {
    return moduleinit();
}
{%- endif %}
