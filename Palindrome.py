
def isPalindrome(word):
    low = 0
    high = len(word) - 1
    word = word.lower()

    while low < high:
        if word[low] != word[high]:
            return False

        low += 1
        high -= 1

    return True

word = input("Enter a String: ")
print(word+ " is a palindrome: "+str(isPalindrome(word)))