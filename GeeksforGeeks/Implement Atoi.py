#User function template for Python
class Solution:
    def myAtoi(self, s):
        # Code here

        i = 0
        n = len(s)
        res = 0
        sign = 1
        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1

        while i < n and s[i] == " ":
            i += 1

        if i < n and (s[i] == "+" or s[i] == "-"):
            sign = -1 if s[i] == "-" else 1
            i += 1

        while i < n and "0" <= s[i] <= "9":
            digit = ord(s[i]) - ord("0")
            res = res * 10 + digit

            if sign * res > INT_MAX:
                return INT_MAX

            if sign * res < INT_MIN: return INT_MIN
            i += 1

        return sign * res