def insertion_sort(arr):
  for i in range(1, len(arr)):
    j = i
    while arr[j - 1] > arr[j] and j > 0:
      arr[j - 1], arr[j] = arr[j], arr[j - 1]
      j -= 1
  return arr

def selection_sort(arr):
  for i in range(len(arr)):
    smallest = i
    for j in range(i + 1, len(arr)):
      if arr[j] < arr[smallest]:
        smallest = j
    arr[i], arr[smallest] = arr[smallest], arr[i]
  return arr

def bubble_sort(arr):
  for i in range(len(arr) - 1):
    has_swapped = False
    for j in range(len(arr) -1, i, -1):
      if arr[j - 1] > arr[j]:
        arr[j - 1], arr[j] = arr[j], arr[j - 1]
        has_swapped = True
    if not has_swapped:
      break
  return arr

def shell_sort(arr):
  gaps = [5, 3, 1]
  for gap in gaps:
    for i in range(gap, len(arr)):
      j = i - gap
      while arr[j + gap] < arr[j] and j >= 0:
        arr[j], arr[j + gap] = arr[j + gap], arr[j]
  return arr

def merge_sort(arr):
  if len(arr) < 2:
    return arr
  first_half = merge_sort(arr[:len(arr) // 2])
  second_half = merge_sort(arr[:len(arr) // 2:])
  return merge(first_half, second_half)

def merge(first_half, second_half):
  result = []
  i = j = 0
  while i < len(first_half) and j < len(second_half):
    if first_half[i] < second_half[j]:
      result.append(first_half[i])
      i += 1
    else:
      result.append(second_half[j])
      j += 1
  while i < len(first_half):
    result.append(first_half[i])
    i += 1
  while j < len(second_half):
    result.append(second_half[j])
    j += 1
  return result

import math

def is_prime(n):
  for i in range(2, math.floor(math.sqrt(n)) + 1):
    if n % i == 0:
      print("No")
      return False
  print("yes")
  return True

is_prime(3)