# palindrome or not
def is_palindrome(n):
    return str(n)==str(n-1)

num=int(input("Enter a number:"))
if is_palindrome(num):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")