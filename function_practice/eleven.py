def palindrome(s):
    s = s.replace(' ', '')
    return s == s[::-1]

print(palindrome("mo m"))
print(palindrome("nurses run"))