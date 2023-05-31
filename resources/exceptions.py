class MyException(Exception): 
  def __init__(self, args):
    self.args = args

try:
  l = [0,1,2]
  print(l[4])
  # print(10/0)
  # raise MyException("My error")
  print("Try executed")
except IndexError:
  print("Exception occurred")
else:
  print("Working successfully")
finally: 
  print("Code executed even if exception or success")
print("Code not executed when there's error") 
