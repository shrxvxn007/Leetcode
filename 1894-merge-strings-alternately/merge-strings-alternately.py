class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a = []
        for x in range(min(len(word1), len(word2))):
            a.append(word1[x])
            a.append(word2[x])
        if len(word1) == len(word2):
            return "".join(a)
        elif len(word1) > len(word2):
            return "".join(a) + word1[min(len(word1), len(word2)):]
        else:
            return "".join(a) + word2[min(len(word1), len(word2)):]