class Solution:
    def reverse(self, x: int) -> int:
        max = 2*32 -1
        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = 0
        while x != 0:
            digit = x % 10
            x //= 10

            
            if rev > 2147483647 // 10:
                return 0

            rev = rev * 10 + digit

        return sign * rev



if __name__ == "__main__":
    x = int(input("Enter a number: "))
    sol = Solution()
    print("Reversed number:", sol.reverse(x))
