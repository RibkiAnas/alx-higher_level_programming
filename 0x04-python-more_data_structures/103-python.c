#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
/**
 * print_python_list - Prints information about a Python list object
 * @p: Pointer to a Python list object
 */
void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *list = (PyListObject *)p;

	printf("[*] Python list info\n");

	/* Check if p is a valid Python list object */
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	/* Get the size of the list */
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	/* Get the allocated memory of the list */
	printf("[*] Allocated = %ld\n", list->allocated);
	/* Iterate over the elements in the list and print their type */
	for (i = 0; i < size; i++)
		printf("Element %ld: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
}

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: Pointer to a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	long int size, i;
	PyBytesObject *bytes = (PyBytesObject *)p;
	char *str;

	printf("[.] bytes object info\n");

	/* Check if p is a valid Python bytes object */
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	/* Get the size of the bytes object */
	size = PyBytes_Size(p);
	str = bytes->ob_sval;
	printf("  size: %ld\n", size);
	/* Print the string representation of the bytes object */
	printf("  trying string: %s\n", str);

	/* Print the first 10 bytes of the bytes object in hexadecimal format */
	if (size > 10)
		size = 10;
	printf("  first %ld bytes:", size + 1);
	for (i = 0; i <= size; i++)
		printf(" %02x", str[i] & 0xff);
	printf("\n");
}
