import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp

# Part 1
def smallest_index(books: list[data.Book], start: int) -> Optional[int]: # the argument books is expected to be a list
    # of instances of the class Book, while the argument start is expected to be an integer, and the function has an
    # optional output of integer
    if start >= len(books) or start < 0: # if there is 1 or fewer books, don't change anything
        return None

    mindex = start # assign mindex the value of start
    for idx in range(start + 1, len(books)): # compares the title of the current book to the next book
        if books[idx].title < books[mindex].title: # if the current book is alphabetically smaller than the next, set it
            #as the new mindex
            mindex = idx
    return mindex # returns the alphabetically smallest book from the given starting point


def alphabetical_sort(books: list[data.Book]) -> None: # argument books is expected to be a list of instances of the
    # class Books, and the function will not output anything because it is modifying the given list
    for idx in range(len(books) - 1): # repeats for total books in the list, except for the last
        mindex = smallest_index(books, idx) # calls the function smallest_index() to get the mindex
        books[mindex], books[idx] = books[idx], books[mindex] # swaps the current book with the alphabetically smallest book

# Part 2
def swap_case(letters: str) -> str: # the argument letters is expected to be a string, and the function will output a string
    final = [] # creates a list called final
    for i in letters: # repeats for every character in the string
        if i.isupper(): # if the character is uppercase, then turn it into lowercase and add it to the final list
            temp = i.lower()
            final.append(temp)
        elif i.islower(): # if the character is lowercase, then turn it into uppercase and add it to the final list
            temp = i.upper()
            final.append(temp)
        else: # otherwise add it to the final list
            final.append(i)
    return "".join(final) # returns the final list with all characters joined to create a string


# Part 3
def str_translate(letters: str, old: str, new: str) -> str: # the argument letters is expected to be a (long) string,
    # while the arguments old and new are expected to be (one character) strings
    letters_list = list(letters) # turns the argument letters from a string into a list of characters
    for i in range(len(letters)): # repeats for the total characters in letters_list
        if letters_list[i] == old: # replaces the old character with the new character
            letters_list[i] = new
    return "".join(letters_list) # returns letter_list with all characters joined to create a string with the new character

# Part 4
def histogram_letters(sentence: str) -> dict: # the argument sentence is expected to be a string, and the function is
    # expected to output a dictionary
    count = {} # creates an empty dictionary
    lst = [x.strip(",") for x in sentence.split(" ")] # creates a list of all words in a sentence and removes commas from the words
    for word in lst: # repeats for every word in lst
        if word not in count: # if the word isn't already in the dictionary, add it with the value 1
            count[word] = 1
        else: # otherwise add 1 to the value of the word in the dictionary count
            count[word] += 1
    return count #returns the dictionary count