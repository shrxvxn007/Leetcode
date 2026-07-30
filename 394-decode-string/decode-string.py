class Solution:
    def decodeString(self, s: str) -> str:
        a = []
        ans = ""
        x = 0
        while x < len(s):
            if s[x].isdigit():
                num = 0
                while x < len(s) and s[x].isdigit():
                    num = num * 10 + int(s[x])
                    x += 1
                a.append(num)
            elif s[x] == "[":
                a.append(ans)
                ans = ""
                x += 1
            elif s[x] == "]":
                prev_ans = a.pop()
                num = a.pop()
                ans = prev_ans + (ans * num)
                x += 1
            else:
                ans += s[x]
                x += 1
        return ans
