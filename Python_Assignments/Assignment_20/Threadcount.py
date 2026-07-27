# ---------------------------------------------------------
# Question:
# Design a Python application that creates three
# threads named Small, Capital and Digits.
# All threads accept a string as input.
# Small:
# Count lowercase characters.
# Capital:
# Count uppercase characters.
# Digits:
# Count numeric digits.
# Each thread should also display:
# Thread ID
# Thread Name
# ---------------------------------------------------------

import threading

def Small(text):
    count = 0

    for character in text:
        if character.islower():
            count = count + 1
    thread = threading.current_thread()

    print("\nThread Name :", thread.name)
    print("Thread ID   :", thread.ident)
    print("Lowercase Characters :", count)

def Capital(text):
    count = 0

    for character in text:
        if character.isupper():
            count = count + 1
    thread = threading.current_thread()

    print("\nThread Name :", thread.name)
    print("Thread ID   :", thread.ident)
    print("Uppercase Characters :", count)

def Digits(text):
    count = 0

    for character in text:
        if character.isdigit():
            count = count + 1
    thread = threading.current_thread()

    print("\nThread Name :", thread.name)
    print("Thread ID   :", thread.ident)
    print("Numeric Digits :", count)

def main():
    text = input("Enter a string : ")

    small_thread = threading.Thread(target=Small,args=(text,),)

    capital_thread = threading.Thread(target=Capital,args=(text,),)

    digits_thread = threading.Thread(target=Digits,args=(text,),)

    small_thread.start()
    capital_thread.start()
    digits_thread.start()

    small_thread.join()
    capital_thread.join()
    digits_thread.join()

    print("\nExit from main")

if __name__ == "__main__":
    main()