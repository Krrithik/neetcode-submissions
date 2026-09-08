class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_values = {}

        for num in nums:
            
            if num not in dict_values:
                dict_values[num] = 1
            else:
                dict_values[num] += 1

        sorted_data = dict(sorted(dict_values.items(), key=lambda item:item[1], reverse=True))

        return list(sorted_data.keys())[:k]