
def display_alphabet_by_code(preference):
    if preference == "lowercase":
        number = 97
        for i in range(26):
            print(chr(number))
            number += 1

    elif preference == "uppercase":
        number = 65
        for i in range(26):
            print(chr(number))
            number += 1

    else:
        print("Preference must be uppercase or lowercase")


print("Uppercase:")
display_alphabet_by_code("uppercase")

print()

print("Lowercase:")
display_alphabet_by_code("lowercase")
print()