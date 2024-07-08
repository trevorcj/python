# function syntax
# return statement


def hello_func():
  return 'Hello Function!'
  # pass

print(hello_func().upper())
print(type(hello_func()))


# passing arguments
def hello(greeting, name='John'): # greeting = positional arg, name = keyword arg
  return f'{greeting}, {name}'

print(hello('Hi', name = 'Pete'))


# positional and keyword arguments
def student_info(*args, **kwargs):
  print(args) # tuple
  print(kwargs) # dictionary

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

# student_info(courses, info)
student_info(*courses, **info)


###################
# PRACTICE PROBLEMS
# 1. Write a Python function to find the maximum of three numbers.

def max_of_three(num1, num2, num3):
  '''Finds the maximum of three numbers'''
  max = num1
  if num2 > max:
    max = num2
  if num3 > max:
    max = num3
  
  return max

# num1 = int(input('Enter a number: '))
# num2 = int(input('Enter a number: '))
# num3 = int(input('Enter a number: '))
print(max_of_three(21, 45.5, 6))


# 2. Write a Python function to sum all the numbers in a list.
# grades = [8, 2, 3, 0, 7]

def sum_all(numbers):
  sum = 0
  
  for x in numbers:
    sum += x
  
  return sum

print(sum_all((8, 2, 3, 0, 7))) # tuple