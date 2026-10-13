from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        r_senators = deque()
        d_senators = deque()

        for i in range(n):
            if senate[i] == 'R':
                r_senators.append(i)
            else:
                d_senators.append(i)
        
        while r_senators and d_senators:
            r = r_senators.popleft()
            d = d_senators.popleft()

            if r < d:
                r_senators.append(r + n)
            else:
                d_senators.append(d + n)
                
        return 'Radiant' if r_senators else 'Dire'