#!/usr/bin/python3
"""Function to print text with 2 new lines after ., ? and :"""


def text_indentation(text):
    """Print text with 2 new lines after ., ? and :

    Args:
        text: The text to print

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(text[i], end="")
            print("\n")
            i += 1
            # Skip spaces after punctuation
            while i < len(text) and text[i] == ' ':
                i += 1
        else:
            print(text[i], end="")
            i += 1
