You can count repeated values in a string in an optimized way using Python's built-in dictionary or the `collections.Counter` class.

Here is an example using a dictionary:
```python
def count_repeated_chars(input_str):
        char_count = {}
            for char in input_str:
                if char in char_count:
                                char_count[char] += 1
                                        else:
                                                        char_count[char] = 1
                                                            return char_count\n\ninput_str = \"hello world\"\nchar_count = count_repeated_chars(input_str)\nprint(char_count)
```
Output:
```python\n{'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
```
Explanation:\n\n* We initialize an empty dictionary `char_count`.\n* We iterate over each character in the input string.\n* For each character, we check if it exists in the `char_count` dictionary.\n* If it does, we increment the count by 1.\n* If it doesn't, we add it to the dictionary with a count of 1.\n* Finally, we return the `char_count` dictionary.\n\nHowever, a more optimized and Pythonic way to achieve this is by using the `collections.Counter` class:\n```python\nfrom collections import Counter\n\ndef count_repeated_chars(input_str):\n    return Counter(input_str)\n\ninput_str = \"hello world\"\nchar_count = count_repeated_chars(input_str)\nprint(char_count)\n```\nOutput:\n```python\nCounter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})\n```\nExplanation:\n\n* We import the `Counter` class from the `collections` module.\n* We define a function `count_repeated_chars` that takes an input string.\n* We return the result of calling `Counter` on the input string.\n* The `Counter` class automatically counts the frequency of each character in the string and returns a dictionary-like object.\n\nBoth of these approaches have a time complexity of O(n), where n is the length of the input string. However, the `collections.Counter` approach is more concise and efficient.