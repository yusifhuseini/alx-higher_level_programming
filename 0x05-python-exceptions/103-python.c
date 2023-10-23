#include <Python.h>

void print_python_float(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_float - function, prints basic info about python float
 * @p: PyObject
 *
 * Return: void
 */
void print_python_float(PyObject *p)
{
	char *s;
	double f;

	printf("[.] float object info\n");

	if (PyFloat_Check(p))
	{
		f = PyFloat_AsDouble(p);
		s = PyOS_double_to_string(f, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
		printf("  value: %s\n", s);
	}
	else
	{
		printf("  [ERROR] Invalid Float Object\n");
	}
}

/**
 * print_python_bytes - function, prints basic info about python bytes
 * @p: PyObject
 *
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	int i;
	char *buffer;
	Py_ssize_t len;

	printf("[.] bytes object info\n");

	if (PyBytes_Check(p))
	{
		len = PyBytes_Size(p);
		buffer = ((PyBytesObject *)(p))->ob_sval;
		printf("  size: %zu\n", len);
		printf("  trying string: %s\n", buffer);
		if (len > 9)
			len = 9;
		printf("  first %zu bytes: ", len + 1);
		for (i = 0; i <= len; i++)
		{
			if (i == len)
				printf("%02x\n", buffer[i] & 0xff);
			else
				printf("%02x ", buffer[i] & 0xff);
		}
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}

/**
 * print_python_list - function, prints some basic info about python list
 * @p: PyObject
 *
 * Return: void
 */
void print_python_list(PyObject *p)
{
	int i;
	PyObject *v;
	PyListObject *list;
	Py_ssize_t len;

	printf("[*] Python list info\n");

	if (PyList_Check(p))
	{
		list = (PyListObject *)(p);

		len = ((PyVarObject *)(p))->ob_size;
		printf("[*] Size of the Python List = %zu\n", len);
		printf("[*] Allocated = %zu\n", list->allocated);

		for (i = 0; i < len; i++)
		{
			v = PyList_GET_ITEM(p, i);
			printf("Element %d: %s\n", i, (v->ob_type)->tp_name);
			if (PyBytes_Check(v))
				print_python_bytes(v);
			else if (PyFloat_Check(v))
				print_python_float(v);
		}
	}
	else
	{
		printf("  [ERROR] Invalid List Object\n");
	}
}

