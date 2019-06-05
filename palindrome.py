string= input("Enter a string: ")

def clean_text(text):
    """
    Given a text, return the text with no spaces or punctuation and all lowercased.
    """
    new_text = ""
    text = text.lower()
    for character in text:
        if character.isalpha():
            new_text = new_text + character
    return new_text

string = clean_text(string)
print(string)

rev_string = string[::-1]

if string == rev_string:
    print("It is a palindrome")
else:
    print("It is not a palindrome")

