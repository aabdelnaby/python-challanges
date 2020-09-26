# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

#solution

def dupliDeleter(x):
  y = []
  for i in x:
    if i not in y:
      y.append(i)
  return y
