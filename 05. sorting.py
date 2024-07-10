# sorting lists
li = [9, 1, 8, 2, 7, 3, 6, 4, 5]

s_li = sorted(li, reverse=True) # returns a new list

print(f'Sorted Variable:   {s_li}')

# li.sort() # doesn't return a new list

print(f'Original Variable: {li}')


# sorting tuples
tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)

s_tup = sorted(tup)

print(f'Sorted Tuple:   {s_tup}')
print(f'Original Tuple: {tup}')


# sorting dictionaries
di = {'name': 'John', 'job': 'Programming', 'age': None, 'os': 'Mac'}
s_di = sorted(di)

print(f'Sorted Dictionary:   {s_di}')
print(f'Original Dictionary: {di}')


li2 = [-6, -5, -4, 1, 2, 3]
s_li2 = sorted(li2, key=abs) # you can create a function amd assign it to key to tell it how to sort
print(s_li2)

# for complex sorting, import attrgetter from operator
# sorted_x = sorted(complex_x, key=attrgetter('...'))