# Required arguments
# keyword arguments
# default arguments - should be placed last
def printer(name1, name2, joiner="&"):
  print(name1, joiner, name2)

printer(name2="Jerry", name1="Tom")

# variable length arguments
def sum(*numbers):
  total = 0
  for n in numbers:
    total += n
  return total

result = sum(1,2,3,4,5)
print('Sum = ', result)

# lambda - anonymous function
sub = lambda x,y: x-y
print(sub(5,2))