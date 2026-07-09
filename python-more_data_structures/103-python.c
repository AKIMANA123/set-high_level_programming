#include <Python.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/**
 * print_python_bytes - prints info about Python bytes objects
 * @p: PyObject bytes object
 */
void print_python_bytes(PyObject *p)
{
Py_ssize_t size, i;
char *str;

printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

size = ((PyVarObject *)p)->ob_size;
str = ((PyBytesObject *)p)->ob_sval;

printf("  size: %ld\n", size);
printf("  trying string: %s\n", str);

if (size >= 10)
printf("  first 10 bytes: ");
else
printf("  first %ld bytes: ", size + 1);

for (i = 0; i < size + 1 && i < 10; i++)
{
printf("%02x", (unsigned char)str[i]);
if (i != size && i != 9)
printf(" ");
}
printf("\n");
}

/**
 * print_python_list - prints info about Python lists
 * @p: PyObject list object
 */
void print_python_list(PyObject *p)
{
Py_ssize_t size, allocated, i;
PyObject *item;

printf("[*] Python list info\n");
if (!PyList_Check(p))
{
printf("  [ERROR] Invalid List Object\n");
return;
}

size = ((PyVarObject *)p)->ob_size;
allocated = ((PyListObject *)p)->allocated;

printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", allocated);

for (i = 0; i < size; i++)
{
item = ((PyListObject *)p)->ob_item[i];
printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
if (PyBytes_Check(item))
print_python_bytes(item);
}
}
