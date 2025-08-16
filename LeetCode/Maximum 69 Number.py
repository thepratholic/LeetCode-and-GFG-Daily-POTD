class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        temp = ""

        f = False
        for i in range(len(num)):
            if num[i] == '6' and not f:
                temp += '9'
                f = True
            else:
                temp += num[i]

        num = int(temp)
        return num