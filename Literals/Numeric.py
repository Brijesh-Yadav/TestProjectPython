#Complex-In the form of a+bj where a forms the real part and b forms
# the imaginary part of the complex number. eg: 3.14j
#Float-Real numbers with both integer and fractional part eg: -26.2
#Integers of unlimited size followed by lowercase or uppercase L eg: 87032845L


x = 0b10100  # Binary Literals
y = 100  # Decimal Literal
z = 0o215  # Octal Literal
u = 0x12d  # Hexadecimal Literal

# Float Literal
float_1 = 100.5
float_2 = 1.5e2

# Complex Literal
a = 5 + 3.14j

print(x, y, z, u)
print(float_1, float_2)
print(a, a.imag, a.real)