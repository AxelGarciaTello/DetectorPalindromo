##
#Determine whether or not a string entered by the user is a palindrome
#using recursion
#

#Determine whether or not a string is a palindrome
#@param s the string to check
#@return True if the string is a palindrome, False otherwise

def isPalindrome(s):
    #Base case: the empty string is a palindrome. So is a string only 1
    #character
    if len(s)<=1:
        return True

    #Recrusive case: The string is a palindrome only if the first and
    #last characters match, and the rest of the string is a palindrome
    return s[0]==s[len(s)-1] and isPalindrome(s[1:len(s)-1])

#Check whether or not a string entered by the user is a palindrome
def main():
    #Read the input from user
    line=input("Enter a string: ")

    #Chech the status and display the result
    if isPalindrome(line):
        print("That was a palindrome!")
    else:
        print("That isn't a palindrome")

#Call the main function
main()
