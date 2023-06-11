#include <Python.h>

/**
 * print_python_list_info - function that
 * prints some basic info about Python lists
 * @p: pointer to a Python object
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t size, i;
	PyObject *item;

	if (PyList_Check(p))
	{
		list = (PyListObject *)p;
		size = PyList_Size(p);
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", list->allocated);
		for (i = 0; i < size; i++)
		{
			item = PyList_GetItem(p, i);
			printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
		}
	}
}
