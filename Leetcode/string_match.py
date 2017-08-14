class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        d = {"*": lambda input_str: True,
             ".": lambda input_str: input_str
             }
        # S to compare with and p conatins the special characters
        # * matches all preceding characters
        # . should match only one character
        if len(s) > 0:
            if ('*','.' not in list(p)):
                return  True if p == s else False
            else:
                for i in range(len(p)):
                    if p[i] not in ["*","."] and i > len(s)-1:
                        if p[i] != s[i]:
                            return False
                    elif p[i] in ["*","."]:
                        print d[p[i]]
                        if d[p[i]] == True:
                            return True
                    return True
        else:
            return False


s = Solution()
r = s.isMatch("aa","a*")
print r