import random
import math
import datetime
import calendar
import os

import antigravity

courses = ['History', 'Math', 'Physics', 'CompSci']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

print('STUDY TIMETABLE')

for day in days:
  # SOLUTION 1
  # to_Study = random.randint(0, (len(courses) - 1))
  # print(f'- {day}: {courses[to_Study]}')
  
  random_course = random.choice(courses)
  print(f'- {day}: {random_course}')



# using the math module
print(math.ceil(5.8))
print(math.floor(5.8))

rads = math.radians(90)
print(math.sin(rads))



# using the datetime module
today = datetime.date.today()
print(today) # todays's date


# using the calendar module
print(calendar.isleap(2024)) # True (Boolean)


# using the os module
print(os.getcwd())

# check their location using their dunder file method
print(os.__file__)
print(datetime.__file__)
print(calendar.__file__)
print(random.__file__)