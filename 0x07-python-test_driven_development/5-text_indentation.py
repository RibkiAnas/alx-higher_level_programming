#!/usr/bin/python3
"""Define a function text_indentation"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :.
    Args:
        text (str): The text to be printed.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    chars = ['.', '?', ':']
    for char in chars:
        text = text.replace(char, char + '\n\n')
    lines = text.split('\n')
    for i, line in enumerate(lines):
        print(line.strip(), end='' if i == len(lines) - 1 else '\n')
