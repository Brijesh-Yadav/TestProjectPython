
import numpy;

a = numpy.array([1,2,3]);
print(a);
print (type(a));

arr = numpy.array([[1,2,3],[5,6,7]],dtype=complex);
print(arr)

print(arr.ndim)

print(a.size)
print("item size ",a.itemsize)