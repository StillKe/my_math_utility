from my_math.functions import *
print(add.my_add(1, 3))
print(mul.my_mul(4, 2))
print(div.my_div(10, 2))

$ cat my_math/__init__.py  # empty file
$ cat my_math/functions/__init__.py
__all__ = ["add", "mul"]