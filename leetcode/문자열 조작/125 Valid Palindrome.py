class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join((s.lower()).split())
        result = ""

        for i in range(len(string)):
            if string[i].isalpha():
                result += string[i]
            elif string[i].isdecimal():
                result += string[i]
        if len(result) % 2 == 0:

            if result[:len(result)//2] == "".join(list(reversed(result[len(result)//2:]))):
                return True
            else:
                return False
        else:
            if result[:len(result)//2] == "".join(list(reversed(result[len(result)//2+1:]))):
                return True
            else:
                return False
