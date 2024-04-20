import math

def double(x):
    return 2 * x

# Print the result of calling the double function with an argument
print(double(5))

# Create a list of functions
myfns = [math.sqrt, int, double, math.cos]

# Print the result of applying the first function (math.sqrt) to 3.14
print(myfns[0](3.14))

# Print the result of applying the second function (int) to 3.14
print(myfns[1](3.14))

# Print the result of applying the third function (double) to 3.14
print(myfns[2](3.14))

# Print the result of applying the fourth function (math.cos) to 3.14
print(myfns[3](3.14))

# Define a function that returns the double function
def doubler():
    return double

# Call the doubler function and then call the returned function on 2.718
print(doubler()(2.718))
