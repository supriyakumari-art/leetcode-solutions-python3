

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def dfs(O, C, s):
            if O == 0 and C == 0:
                res.append(s)
                return

            if O > 0:
                dfs(O - 1, C, s + "(")

            if C > O:
                dfs(O, C - 1, s + ")")

        dfs(n, n, "")
        return res
