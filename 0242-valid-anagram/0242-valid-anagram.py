class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        arr1 = list(s)
        arr2 = list(t)

        arr1.sort()
        arr2.sort()

        for i in range(len(arr1)):
            if arr1[i] != arr2[i]:
                return False

        return True