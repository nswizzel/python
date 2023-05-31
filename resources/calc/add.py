import sys

sum = 0

def addFn(n1, n2):
  return int(n1) + int(n2)

if __name__ == "__main__":
  print(addFn(sys.argv[1], sys.argv[2]))

# import module
"""
...\resources\calc> python
>>> import add
>>> add.addFn(1,2)
3
"""

# import function from module
"""
>>> from add import addFn
>>> addFn(1,2)
3
"""

# import all function from module
"""
>>> from add import *
>>> addFn(1,2)
3
>>> sum
0
"""
#executing module as script
""""
...\calc> python add.py 1 2
"""
