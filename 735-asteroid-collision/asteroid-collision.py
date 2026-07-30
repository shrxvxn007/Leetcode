from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        a = []
        for x in asteroids:
            if x > 0:
                a.append(x)
            else:
                if len(a) == 0 or a[-1] < 0:
                    a.append(x)
                    continue
                
                while len(a) != 0 and a[-1] > 0 and abs(x) > a[-1]:
                    a.pop()
                if len(a) == 0 or a[-1] < 0:
                    a.append(x)
                elif abs(x) < a[-1]:
                    pass  
                else:
                    a.pop()
        return a
