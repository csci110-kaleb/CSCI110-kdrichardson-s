#I used google to check if my answer was correct because I still do not know how to unit test and for some reason kattis test says its wrong but kattis submit says its right.
import sys

def get_alphabet_mapping():
    """Returns a dictionary mapping lowercase letters to their new alphabet symbols."""
    return {
        'a': '@',      'b': '8',      'c': '(',      'd': '|)',     'e': '3',
        'f': '#',      'g': '6',      'h': '[-]',    'i': '|',      'j': '_|',
        'k': '|<',     'l': '1',      'm': r'[]\/[]', 'n': r'[]\[]', 'o': '0',
        'p': '|D',     'q': '(,)',    'r': '|Z',     's': '$',      't': "']['",
        'u': '|_|',    'v': r'\/',    'w': r'\/\/','x': '}{',     'y': '`/',
        'z': '2'
    }

def translate_text(text, mapping):
    """Translates the given text character by character using the mapping dictionary."""
    translated_chars = []
    
    for char in text:
        # Convert to lowercase to ensure case-insensitivity
        lower_char = char.lower()
        
        # If the character is in our dictionary, use its translation; otherwise, keep it
        if lower_char in mapping:
            translated_chars.append(mapping[lower_char])
        else:
            translated_chars.append(char)
            
    return "".join(translated_chars)

def main():
    # Read the full line of text from standard input (required for Kattis)
    input_text = sys.stdin.read()
    
    # Initialize the dictionary and translate the text
    mapping = get_alphabet_mapping()
    result = translate_text(input_text, mapping)
    
    # Print the final translated result
    print(result, end='')

if __name__ == "__main__":
    main()