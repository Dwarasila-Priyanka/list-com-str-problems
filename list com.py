#1. Rotate a list by k positions to the right.
# Input: lst = [1, 2, 3, 4, 5], k = 2
# Output: [4, 5, 1, 2, 3]

def rotate_list(lst, k):
    k = k % len(lst) 
    return lst[-k:] + lst[:-k]
print(rotate_list([1, 2, 3, 4, 5], 2)) 

#2.Remove all duplicates from a list without using set().
# Input: [1, 2, 3, 2, 1, 4, 5]
# Output: [1, 2, 3, 4, 5]
def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result
print(remove_duplicates([1, 2, 3, 2, 1, 4, 5]))  

#3.Find all pairs in a list that sum up to a target.
# Input: lst = [2, 4, 3, 5, 7], target = 7
# Output: [(2, 5), (4, 3)]
def find_pairs(lst, target):
    pairs = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target:
                pairs.append((lst[i], lst[j]))
    return pairs
print(find_pairs([2, 4, 3, 5, 7],7))

#4.Flatten a 2D list without using built-in flatten functions.
# Input: [[1, 2], [3, 4], [5]]
# Output: [1, 2, 3, 4, 5]

def flatten_2d_list(lst):
    result = []
    for sublist in lst:
        for item in sublist:
            result.append(item)
    return result
print(flatten_2d_list([[1, 2], [3, 4], [5]]))  

#5.Count the frequency of each element in a list and return a dictionary.
# Input: [1, 2, 2, 3, 1, 4, 2]
# Output: {1: 2, 2: 3, 3: 1, 4: 1}

def count_frequencies(lst):
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq
print(count_frequencies([1, 2, 2, 3, 1, 4, 2]))  

#6.Check if a string is a palindrome (ignoring spaces and case).
# Input: "A man a plan a canal Panama"
# Output: True

def is_palindrome(s):
    cleaned = ""
    for ch in s:
        if ch != " ":
            cleaned += ch.lower()
    return cleaned == cleaned[::-1]
print(is_palindrome("A man a plan a canal Panama"))  

#7.Find the first non-repeating character in a string.
# Input: "aabbcdeff"
# Output: 'c'

def first_non_repeating_char(s):
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    for ch in s:
        if freq[ch] == 1:
            return ch
    return None  
print(first_non_repeating_char("aabbcdeff"))  

#8.Remove all vowels from a string.
# Input: "Hello World"
# Output: "Hll Wrld"

def remove_vowels(s):
    vowels = 'aeiouAEIOU'
    result = ''
    for ch in s:
        if ch not in vowels:
            result += ch
    return result
print(remove_vowels("Hello World")) 

#9.Count the number of words in a string without using .split().
# Input: "Python is great"
# Output: 3

def count_words(s):
    in_word = False
    count = 0
    for ch in s:
        if ch != ' ' and not in_word:
            in_word = True
            count += 1
        elif ch == ' ':
            in_word = False
    return count

print(count_words("Python is great"))  

#9.Find the longest word in a sentence.
# Input: "The quick brown fox jumps over the lazy dog"
# Output: "jumps"

def longest_word(s):
    word = ''
    max_word = ''
    for ch in s + ' ':  # Add a space to capture the last word
        if ch != ' ':
            word += ch
        else:
            if len(word) > len(max_word):
                max_word = word
            word = ''
    return max_word
print(longest_word("The quick brown fox jumps over the lazy dog"))










