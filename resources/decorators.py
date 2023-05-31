import time

def timing(fn):
  def wrapper(*args, **kwargs):
    print("Start")
    t1 = time.time()
    fn(*args, **kwargs)
    t2 = time.time()
    print("End")
    return str(t2 - t1)
  return wrapper

@timing
def printer(s):
  time.sleep(2)
  print(s)

"""
terminal
In [2]: from user.decorators import *

In [3]: printer("Hello world!")
Start
Hello world!
End
Out[3]: '2.0016558170318604'

In [4]:
""""