# O(n)
def linear_search(list, target):
  """
  Retruns the index of the target if found, else returns None
  """
  
  for i in range(0, len(list)):
    if list[i] == target:
      return i
  return None

def verify(index):
  if index is not None:
    print(f"Target found at index: {index}")
  else:
    print(f"Target not found in list")

# O(logn)
def binary_search(list, target):
  first = 0
  last = len(list) - 1
  
  while first <= last:
    midpoint = (first + last) // 2
    if  list[midpoint] == target:
      return midpoint
    elif list[midpoint] < target:
      first = midpoint + 1
    else:
      last = midpoint - 1
  return None

def verify(index):
  if index is not None:
    print(f"Target found at index: {index}")
  else:
    print(f"Target not found in list")

# 
def recursive_binary_search(list, target):
  if len(list) == 0:
    return False
  else:
    midpoint = (len(list)) // 2
    if list[midpoint] == target:
      return True
    else:
      if list[midpoint] < target:
        return recursive_binary_search(list[midpoint + 1:], target)
      else:
        return recursive_binary_search(list[:midpoint], target)

def verify_recusion(result):
  print("Target found: ", result)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = recursive_binary_search(numbers, 6)
verify_recusion(result)