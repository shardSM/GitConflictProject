value = input("Enter a word or phrase: ")
clean_value = "".join(value.lower().split())

if clean_value == clean_value[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")