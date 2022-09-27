class Solution:
    def conv_bi(self, a: str) -> int():
        sum = 0
        for i in range(len(a)):
            sum += int(a[-1-i])*(2**i)
        return sum
        
    def addBinary(self, a: str, b: str) -> str:
        num_sum = self.conv_bi(a) + self.conv_bi(b)
        if num_sum == 0:
            return "0"
        upper_limit = 0
        res = ''
        while num_sum > 2**upper_limit:
            upper_limit += 1
        for i in range(upper_limit, -1, -1):
            if i == upper_limit and num_sum // 2**i == 0:
                continue
            else:
                res += str(num_sum // 2**i)
                num_sum = num_sum % 2**i
        return res

if __name__ == "__main__":
    sol = Solution()
    ans = sol.addBinary('1010', '1011')
    print(ans)
