class Example:
   __instance = None
   @staticmethod 
   def instance():
      if Example.__instance == None:
         Example()
      return Example.__instance
   def __init__(self):
      if Example.__instance != None:
         raise Exception("Esto es un singleton")
      else:
         Example.__instance = self
test = Example()
print(test)

test = Example.instance()
print(test)