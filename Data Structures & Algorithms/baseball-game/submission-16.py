class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []
        ans = 0
        for i in operations:
            if i == "+" and len(s) > 1:
                s.append((s[-1]+s[-2]))
            elif i == "C":
                s.pop()
            elif i == "D":
                s.append((s[-1]*2))
            else:
                s.append(int(i))  
                print(s)
        print(s)
        
        return sum(s)
            
        