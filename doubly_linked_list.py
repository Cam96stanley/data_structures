class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.previous = None
    
class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self._length = 0
    
  def append(self, value):
    new_node = Node(value)
    if not self._length:
      self.head = self.tail = new_node
    else:
      self.tail.next = new_node
      new_node.previous = self.tail
      self.tail = new_node
    self._length += 1
    return self
  
  def prepend(self, value):
    new_node = Node(value)
    if not self._length:
      self.head = self.tail = new_node
    else:
      new_node.next = self.head
      self.head.previous = new_node
      new_node = self.head
    self._length += 1
    return self
  
  def pop_left(self):
    if not self._length:
      raise Exception("list is empty")
    prev_head = self.head
    if self._length == 1:
      self.head = self.tail = None
    else:
      self.head = prev_head.next
      prev_head.next = None
    self.head.previous = None
    self._length -= 1
    return prev_head.value
  
  def pop_right(self):
    if not self._length:
      raise Exception("list is empty")
    old_tail = self.tail
    if self._length == 1:
      self.head = self.tail = None
    else:
      self.tail = old_tail.previous
      old_tail.previous = None
      self.tail.next = None
    self._length -= 1
    return old_tail.value
  
  def remove(self, value):
    if not self._length:
      raise Exception("list is empty")
    if self.head.value == value:
      return self.pop_left()
    prev_node = self.head
    current_node = self.head.next
    while current_node is not None and current_node != value:
      prev_node = current_node
      current_node = current_node.next
    if current_node is None:
      raise ValueError("item not in list")
    if current_node.next is None:
      return self.pop_right()
    current_node.next.previous = prev_node
    prev_node.next = current_node
    current_node.previous = None
    current_node.next = None
    self._length -= 1
    return current_node.value