# import mymodule as mm
# from mymodule import find_index as fi
# from mymodule import *
import sys
# sys.path.append('/Users/Administrator/Desktop/')
from mymodule import find_index, test

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
# print(index)
# print(test)

# for index, value in enumerate(courses):
#   print(index, value)

print(sys.path)