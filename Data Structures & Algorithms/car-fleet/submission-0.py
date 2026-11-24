class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position, speed)]
        
        stack = []
        for p,s in sorted(pair)[::-1]:  # reverse sorted order because the input is given in randam position point data
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:  # older time is more and will collide with the new one, making it a fleet
                stack.pop()

        return len(stack)