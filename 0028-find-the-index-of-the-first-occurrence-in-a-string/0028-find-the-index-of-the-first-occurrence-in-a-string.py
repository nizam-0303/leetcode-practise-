class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = 0

        while l < len(haystack):
            r = l          
            c = 0

            for k in range(len(needle)):
                if r >= len(haystack):
                    break

                if haystack[r] == needle[k]:
                    r += 1
                    c += 1
                else:
                    break

            if c == len(needle):
                return l

            l += 1

        return -1