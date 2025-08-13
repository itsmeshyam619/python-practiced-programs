a = [1, 2, 3, 4, 5, 6]

# First, filter even numbers
b = filter(lambda x: x % 2 == 0, a)
print(b)
#print(list(b))
print(b)
# Then, double the filtered numbers
c = list(map(lambda x: x * 2, b))
print(tuple(a))

''' filter function requires two arguments
d=filter(map(lambda x : x*2 if x%2==0 else x*0 , a))

print(list(d))
'''
numbers = [1, 2, 3, 4, 5, 6]
squared_even = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print(squared_even)  # Output: [4, 16, 36]

print(c)

