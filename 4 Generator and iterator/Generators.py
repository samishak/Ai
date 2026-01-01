def square(n):
    for i in range(3):
        yield i ** 2
print(square(3))
# Output: <generator object square at 0x7f9d8c0b8b80>
#print(list(square(3)))
# Output: [0, 1, 4]
for num in square(3):
    print(num)
# yield	                return
# Pauses function	   Ends function
# Remembers state	   Loses state
# Used in generators	Used in normal functions

print ("--------------------")
a=square(5)
print(next(a))  # Output: 0
print(next(a))  # Output: 1

#for reading a large file allowing pricess ine line without loading the entire file into memory