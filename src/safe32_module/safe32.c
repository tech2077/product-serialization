#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <safe32/safe32.h>

static PyObject* safe32_safe32_encode(PyObject* self, PyObject *args)
{
    char* input_buf = NULL;
    char* output_buf = NULL;
    Py_ssize_t input_buf_len = 0, output_buf_len = 0;
    
    if (!PyArg_ParseTuple(args, "s#", &input_buf, &input_buf_len)) {
        // error, we should do something about this
    }

    output_buf = (char*)malloc(input_buf_len * 2);

    if ((output_buf_len = safe32_encode((uint8_t*)input_buf, input_buf_len, (uint8_t*)output_buf, input_buf_len * 2)) < 0) {
        // error, we should do something about this
    }

    PyObject *output_bytes = PyBytes_FromStringAndSize(output_buf, output_buf_len);

    free(output_buf);

    return output_bytes;
}

static PyObject* safe32_safe32_decode(PyObject* self, PyObject *args)
{
    char* input_buf = NULL;
    char* output_buf = NULL;
    Py_ssize_t input_buf_len = 0, output_buf_len = 0;
    
    if (!PyArg_ParseTuple(args, "s#", &input_buf, &input_buf_len)) {
        // error, we should do something about this
    }

    output_buf = (char*)malloc(input_buf_len * 2);

    if ((output_buf_len = safe32_decode((uint8_t*)input_buf, input_buf_len, (uint8_t*)output_buf, input_buf_len * 2)) < 0) {
        // error, we should do something about this
    }

    PyObject *output_bytes = PyBytes_FromStringAndSize(output_buf, output_buf_len);

    free(output_buf);

    return output_bytes;
}

static PyMethodDef methods[] = {
    {"safe32_encode", (PyCFunction)safe32_safe32_encode, METH_VARARGS, NULL},
    {"safe32_decode", (PyCFunction)safe32_safe32_decode, METH_VARARGS, NULL},
    {NULL, NULL, 0, NULL},
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "safe32",
    NULL,
    -1,
    methods,
};

PyMODINIT_FUNC PyInit_safe32(void)
{
    return PyModule_Create(&module);
}
