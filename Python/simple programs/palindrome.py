def palindrome(n):
    if n == n[::-1]:
        return True

    else:
        return False

n = input("Enter a plaindrome: ")
palin = palindrome(n)
if palin == True:
    print("This is a palindrome")
else:
    print("This is not a palindrome")
