print('Imported mymodule...')

test = 'Test String'

def find_index(to_search, target):
  '''Finds the index of a value'''
  for i, value in enumerate(to_search):
    if value == target:
      return i
  
  return -1