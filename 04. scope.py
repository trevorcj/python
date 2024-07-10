'''
LEGB
Local, Enclosing, Global, Built-in
'''

# x = 'global x'

# def test():
#   # y = 'local y'
#   # print(y)
#   global x
#   x = 'local x'
#   print(x)
  
# test()
# print(x)
# print(y)


# Enclosing
def outer():
  x = 'outer x'
  
  def inner():
    nonlocal x
    x = 'inner x'
    print(x)
    
  inner()
  print(x)

outer()