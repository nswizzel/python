from .decorators import is_new_account

class Account():
  accounts = []
  id = 0
  # every method inside a class must have self(instance) 
  def __init__(self, id=None):  
    print("constructor is called")
    self.id = Account.id

  def get(self):
    # pass - used instead of function definition
    if self.id:
      for a in Account.accounts:
        if a["id"] == self.id:
          return a
    else:
      print("Account is not yet created")

  @is_new_account
  def create(self, data):
    Account.id += 1
    data["id"] = Account.id
    Account.accounts.append(data)
    self.id = Account.id

  def update(self, password=None):
    if self.id:
      for a in Account.accounts:
        if a["id"] == self.id:
          a["password"] = password
          break
    else:
      print("Account is not yet created")

  def delete(self):
    if self.id:
      for a in Account.accounts:
        if a["id"] == self.id:
          Account.accounts.remove(a)
          break
    else:
      print("Account is not yet created")
