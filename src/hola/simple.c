#include <Python.h>

static PyObject* simple_hola(PyObject* self, PyObject* args){
    char *msg = "Hola Panamá";
    return Py_BuildValue("s", msg);
}

static char simple_docs[] =
    "hola(): imprime hola\n";

static PyMethodDef funciones[] = {
    {"hola", (PyCFunction)simple_hola, METH_NOARGS, simple_docs},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef modulo = {
    PyModuleDef_HEAD_INIT, "simple", NULL, -1, funciones
};

PyMODINIT_FUNC PyInit_simple(void){
    return PyModule_Create(&modulo);
}
