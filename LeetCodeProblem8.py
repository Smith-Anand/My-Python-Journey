class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()          # remove leading spaces
        if not s:
            return 0

        sign = 1
        i = 0

        # check sign
        if s[0] == '-':
            sign = -1
            i = 1
        elif s[0] == '+':
            i = 1

        result = 0

        while i < len(s) and s[i].isdigit():
            digit = ord(s[i]) - ord('0')

            # overflow check
            if result > 2147483647 // 10 or (
                result == 2147483647 // 10 and digit > 7
            ):
                return 2147483647 if sign == 1 else -2147483648

            result = result * 10 + digit
            i += 1

        return sign * result


# ---- driver code (needed for VS Code) ----
if __name__ == "__main__":
    s = input("Enter string: ")
    sol = Solution()
    print("Output:", sol.myAtoi(s))
