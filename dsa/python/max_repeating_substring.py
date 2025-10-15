class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k = 0
        buf = word
        while True:
            if buf in sequence:
                k += 1
                buf += word
            else:
                return k 
        