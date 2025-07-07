def factorial(n):
  if n == 0:
    return 1
  return n * factorial(n-1)

factorial(5)

def fib(n):
  if n <= 2:
    return 1
  return fib(n - 1) + fib(n - 2)

fib(5)

def array_product(arr):
  if not arr:
    return 1
  return arr[0] * array_product(arr[1:])

# Recursion requires call stack management, can use more memory because of all the stack frames, some languages optimize recursive calls, usually has the advantage in code simplicity.

# What to consider in determining the complexity of recursive fn:
# the number of stack frames
# the number of recursive calls
# the other operations done inside the fn
# the space complexity (max num of stack frames)