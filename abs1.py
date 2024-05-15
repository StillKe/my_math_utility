# Define the my_abs function
def my_abs(x):
    if isinstance(x, int) or isinstance(x, float):
        if x >= 0:
            return x
        else:
            return -x
    elif isinstance(x, complex):
        return (x.real**2 + x.imag**2)**0.5
    else:
        raise TypeError("Unsupported operand type for my_abs(): " + str(type(x)))

# Call the my_abs function with an argument
result = my_abs(-5)

# Print the result
print("The absolute value of -5 is:", result)
