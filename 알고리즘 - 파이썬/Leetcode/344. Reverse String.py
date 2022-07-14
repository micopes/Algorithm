# 이 문제는 메모리 제한이 있어서(O(1)) s[::-1]를 하면 신규 변수할당을 하기 때문에 Wrong 이 나옴.
class Solution:
    def reverseString(self, s: List[str]) -> None:
        return s.reverse()