def is_new_account(fun):
  def wrapper(*args, **kwargs):
    self_obj = args[0]
    data = args[1]
    if not self_obj.id:
      if "username" in data.keys():
        for a in self_obj.__class__.accounts:
          if a["username"] == data["username"]:
            return "Username not available"
        fun(*args, **kwargs)
      else:
        print("Provide username")
    else:
      print("Only one account can be created")
  return wrapper

