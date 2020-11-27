import re

def isPalindrome(s: str) -> bool:
    
    #함수의 대문자를 소문자로 바꾸기
    s = s.lower()
    #정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]','',s)
    #리스트 슬라이싱 - 배열 뒤집기
    return s == s[::-1]
    
mysting = "wow"
print(isPalindrome(mysting))
