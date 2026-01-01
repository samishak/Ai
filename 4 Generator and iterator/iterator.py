my_list = [1, 2, 3, 4, 5]
my_iterator = iter(my_list)
print(next(my_iterator))  # Output: 1
print(next(my_iterator))  # Output: 2
print(next(my_iterator))  # Output: 3
print(next(my_iterator))  # Output: 4
print(next(my_iterator))  # Output: 5
# print(next(my_iterator))  # This will raise StopIteration

try:
    print(next(my_iterator))  # This will raise StopIteration
except StopIteration:
    print("Reached the end of the iterator.")  # Output: Reached the end of the iterator.
    
#iterator is for efficient looping through large data sets without loading everything into memory at once.
