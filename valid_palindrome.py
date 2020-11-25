import re

def isPalindrome(s: str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]','',s)
    return s == s[::-1]
    
mysting = "wow"
print(isPalindrome(mysting))
