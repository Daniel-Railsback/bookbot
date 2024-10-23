def main(): # Must define to allow organization & ability to call
    try: # Adding try to catch errors
        book_path = "books/frankenstein.txt" # Hardcode path to a book to read
        text = get_book_text(book_path) # Set string = ALL book text 
        num_words = count_words(text)
        print(f"{num_words} words found in the document")# Print book text stored inside string
    except Exception as msg:
        print(msg)


def get_book_text(path): # Function to open and read file
    try: 
        with open(path) as f: # Open file path saved in path (line 2)
            text = f.read() # Read bytes from file.  This allows line 3 not to error
            # f.close()  # This is how you close the file.  It is no longer needed but important to understand
            return text
    except Exception as msg:
        print(msg)



def count_words(text):
    try:
        # Split 
        words = text.split()
        num_words = len(words)
        return num_words
    except Exception as msg:
        print(msg)


## def count_characters
main() # Call main function defined on line 1 -4

