# fizz buzz
for i in range(1, 20):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

        
# Queue
class queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

# Stacks
class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        l = len(self.items)-1
        return self.items[l]
    def size(self):
        return len(self.items)


# Validate Anagrams
def anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    return sorted(word1) == sorted(word2)

print(anagram("cinema", "iceman"))
print(anagram("cool", "loco"))
print(anagram("men", "women"))

          
# Get Palindrome words in a sentence
def get_palindrome_words(sentence):
    for i in (",.'?/><}{{}}'"):
        sentence = sentence.replace(i, "")
    palindrome = []
    words = sentence.split(' ')
    for word in words:
        word = word.lower()
        if word == word[::-1]:
            palindrome.append(word)
    return palindrome
  
  
# Big O notation
https://www.bigocheatsheet.com/
  
# How does computers works?

# Time and Space complexity?

# Why can't we have slow algorithms?

# Why can't we have algorithms which takes a lot of space?

# O(N)
def example(arr):
    for i in arr: 
    print(i) 
    

# O(N^2)
def example(arr):
    for x in arr:
        for y in arr:
            print(x, y)


# O(1)
def getFirst(arr):
    return arr[0]


# Sorting Visually explained
https://visualgo.net/en/sorting?slide=1

# Bubble Sort
def bubble_sort(lst):
    """
    Bubble sort function
    :param lst: lst of unsorted integers
    """

    # Traverse through all list elements
    for i in range(len(lst)):

        # Last i elements are already in place
        for j in range(0, len(lst) - i - 1):

            # Traverse the list from 0 to size of lst - i - 1
            # Swap if the element found is greater than the next element
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


lst = [3, 2, 1, 5, 4]
bubble_sort(lst)  # Calling bubble sort function
print("Sorted list is: ", lst)
    

   
# Selection Sort
def selection_sort(lst):
    """
    Selection sort function
    :param lst: List of integers
    """

    # Traverse through all lst elements
    for i in range(len(lst)):
        # Find the minimum element in unsorted lst
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j

        # Swap the found minimum element with the first element
        lst[i], lst[min_index] = lst[min_index], lst[i]



lst = [3, 2, 1, 5, 4]
selection_sort(lst)  # Calling selection sort function

# Printing Sorted lst
print("Sorted lst: ", lst)
   

    
# Insertion Sort
def insertion_sort(lst):
    """
    Insertion sort function
    :param lst: lst of unsorted integers
    """

    # Traverse through 1 to len(lst)
    for i in range(1, len(lst)):

        key = lst[i]

        # Move elements of lst greater than key, to one position ahead
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key



lst = [3, 2, 1, 5, 4]
insertion_sort(lst)  # Calling insertion sort function

print("Sorted list is: ", lst) 



# Searching Visually explained

https://www.cs.usfca.edu/~galles/visualization/Search.html


# Linear Search

def linear_search(lst, key):
    """
    Linear search function
    :param lst: lst of unsorted integers
    :param key: A key to be searched in the list
    """
    if len(lst) <= 0:  # Sanity check
        return -1

    for i in range(len(lst)):
        if lst[i] == key:
            return i  # If found return index
    return -1  # Return -1 otherwise



lst = [5, 4, 1, 0, 5, 95, 4, -100, 200, 0]
key = 95

index = linear_search(lst, key)
if index != -1:
    print("Key:", key, "is found at index:", index)
else:
    print(key, " is not found in the list.")


# Binary search

def binary_search(lst, left, right, key):
    """
    Binary search function
    :param lst: lst of unsorted integers
    :param left: Left sided index of the list
    :param right: Right sided index of the list
    :param key: A key to be searched in the list
    """

    while left <= right:

        mid = left + (right - left) // 2

        # Check if key is present at mid
        if lst[mid] == key:
            return mid

        # If key is greater, ignore left half
        elif lst[mid] < key:
            left = mid + 1

        # If key is smaller, ignore right half
        else:
            right = mid - 1

    # If we reach here, then the element was not present
    return -1


lst = [1, 2, 3, 10, 20, 40, 111, 244, 14444, 800000]
key = 111

# Function call
result = binary_search(lst, 0, len(lst) - 1, key)

if result != -1:
    print("Element is present at index:", result)
else:
    print("Element is not present in the list")