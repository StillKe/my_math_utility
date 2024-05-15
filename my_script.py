# Import specific functions from the my_math package
from my_math.abs import my_abs
from my_math.functions.add import add
from my_math.functions.sub import sub
from my_math.functions.mul import mul
from my_math.functions.div import div

# Call the math functions
result_abs = my_abs(-5)
result_add = add(5, 3)
result_sub = sub(5, 3)
result_mul = mul(5, 3)
result_div = div(6, 3)

# Print the results
print("Absolute value of -5:", result_abs)
print("Addition of 5 and 3:", result_add)
print("Subtraction of 5 from 3:", result_sub)
print("Multiplication of 5 and 3:", result_mul)
print("Division of 6 by 3:", result_div)
