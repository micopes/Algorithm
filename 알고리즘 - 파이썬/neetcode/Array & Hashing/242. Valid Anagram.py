class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        li_s = list(s)
        li_t = list(t)

        li_s.sort()
        li_t.sort()

        sorted_s = "".join(li_s)
        sorted_t = "".join(li_t)

        if sorted_s == sorted_t:
            return True
        else:
            return False
