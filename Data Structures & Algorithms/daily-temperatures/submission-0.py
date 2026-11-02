class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # stored in pair (index, temp)
        for i,val in enumerate(temperatures):
            while stack and val > stack[-1][1]:
                stackInd, stackTemp = stack.pop()
                result[stackInd] = i - stackInd
            stack.append((i,val))
        return result       # no need to fill 0's , already we create 0 list with the len(temperatures)
        