class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups_dict = {}

        for i in strs:
            sorted_key = "".join(sorted(i))

            if sorted_key not in groups_dict:
                groups_dict[sorted_key] = []

            groups_dict[sorted_key].append(i)
        
        grouped = list(groups_dict.values())

        return grouped


        