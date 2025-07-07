def array_product(arr):
  total = 1
  for n in arr:
    total *= n
  print(total)

array_product([1, 2, 3, 4, 5])

# In most languages iteration is faster, manual management of a stack in iteration can be error-prone.