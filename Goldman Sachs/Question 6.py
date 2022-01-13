
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        if m == n:
            if str1 == str2:
                return str1
            else:
                return ""
        elif m > n:
            if str1[ : n] != str2:
                return ""
            else:
                return self.gcdOfStrings(str1[n : ], str2)
        else:
            if str2[ : m] != str1:
                return ""
            else:
                return self.gcdOfStrings(str2[m : ], str1)
